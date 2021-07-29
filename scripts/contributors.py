# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

"""
"""

import ast
import datetime
import os
import sys
import time
from typing import Optional
import csv

import requests
from crowdin_api import CrowdinClient


class FirstCrowdinClient(CrowdinClient):
    TOKEN = os.environ.get("CROWDIN_API")
    PAGE_SIZE = 100000  # Optional, sets default page size


client = FirstCrowdinClient()


def get_project_data(project_id: int = 409874):
    """
    Get the crowdin project data.

    Parameters
    ----------
    project_id : int, optional
        Crowdin project identifier Default is `409874`.

    Returns
    -------
    dict
        Crowdin project data.
    """
    result = client.projects.get_project(project_id)
    return result["data"]


def get_languages(project_data):
    """
    Get the available languages for the crowdin project.

    Parameters
    ----------
    project_data : dict
        Crowdin project data.

    Returns
    -------
    dict
        Available languages on crowdin.
    """
    result = {}
    for language in project_data["targetLanguages"]:
        result[language["locale"]] = {"id": language["id"], "name": language["name"]}

    return result


def download_data(project_id=409874, language_id=None):
    """
    Download crowdin contributor data per language.

    Parameters
    ----------
    project_id : int, optional
        Crowdin project identifier Default is `409874`.
    language_id : int, optional
        Crowdin language locale id.

    Returns
    -------
    dict
        Data.
    """
    date_from = datetime.datetime(2019, 4, 1).isoformat() + "Z"
    report = client.reports.generate_top_members_report(
        project_id, "words", languageId=language_id, format="csv", dateFrom=date_from
    )
    report_id = report["data"]["identifier"]

    result = client.reports.check_report_generation_status(project_id, report_id)
    eta = result["data"]["eta"]
    if eta is None:
        unit = "none"

    amount, unit = eta.split(" ")
    if unit == "second":
        wait_time = int(amount) * 2
    else:
        wait_time = 5

    time.sleep(wait_time)

    result = client.reports.download_report(project_id, report_id)
    url = result["data"]["url"]

    r = requests.get(url)
    return r.content.decode("utf-8")


def format_data(data: dict, language: str = None):
    """
    Format the data from crowdin report.

    Parameters
    ----------
    data : dict
        PASSCrowdin data.
    language : str
        Language locale.

    Returns
    -------
    str
        Formated crowdin contributor data.
    """
    new_lines = ["# Contributors", ""]
    lines = [line for line in data.split("\n")[1:] if line]

    # Name,Languages,"Translated (Words)","Target Words","Approved (Words)",Voted,"""+"" votes received","""-"" votes received","Winning (Words)"
    for row in csv.reader(lines, delimiter=","):
        name_or_username = row[0]
        languages = [part.strip() for part in row[1].split(";")]
        words = int(row[2])

        try:
            name_or_username = ast.literal_eval(name_or_username)
        except Exception:
            pass

        if "(" in name_or_username:
            name, username = name_or_username.split("(")
            name = name.strip()
            username = username.split(")")[0].strip()
        else:
            name = ""
            username = name_or_username.strip()

        # print(name, username, languages, words)

        if language is None:
            condition = words > 0
        else:
            condition = language in languages and words > 0

        if condition:
            if name:
                new_lines.append(
                    f"* {name} ([@{username}](https://crowdin.com/profile/{username}))"
                )
            else:
                new_lines.append(
                    f"* {username} ([@{username}](https://crowdin.com/profile/{username}))"
                )

    new_lines.append("")

    return "\n".join(new_lines)


def get_contributors_report(
    project_id: int = 409874, locale: Optional[str] = None
) -> str:
    """
    Get the translators report per word for a given locale language.

    Parameters
    ----------
    project_id : int
        Crowding project identifier.
    locale : str, optional
        Loale string. Default is `None`.

    Returns
    -------
    str
        The formated string for the contributors file.
    """
    data = get_project_data(project_id)
    if locale:
        language_id = get_languages(data)[locale]["id"]
    else:
        language_id = None

    data = download_data(language_id=language_id)

    return format_data(data)


if __name__ == "__main__":
    locale = sys.argv[1]
    print(get_contributors_report(locale=locale))

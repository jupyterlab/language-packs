��          �       �      �     �     �     �     �     �     �     �       L   &     s     �     �     �     �  '   �  =  �  1   /  (   a  ?   �     �     �  0  �  0  -     ^     f  	   w  "   �     �     �     �     �  T   �     S	     d	     u	     �	     �	  /   �	  P  �	  >   /  "   n  7   �     �     �  -  �   %1 [%2] %1 [%2] (online) Adjust spelling to Choose spellchecker language Dictionary not loaded Ignore Language of the spellchecker Loading dictionary… MIME types for files/editors for which the spellchecking should be activated No spellcheck suggestions Online dictionaries Spell Checker Theme Toggle spellchecker Words to be ignored by the spellchecker schemaA list of online dictionaries to use if installing dictionaries in data path of jupyter-server is not possible or not desirable. For example:

[
    {
        "id": "pl_PL-online",
        "aff": "http://some-url/pl_PL.aff",
        "dic": "http://some-url/pl_PL.dic",
        "name": "polski (Polska)"
    }
] schemaCase-sensitive list of words to be ignored schemaDictionary identifier, e.g. en-us schemaList of MIME types. GFM denotes GitHub Flavored Markdown schemaSpellchecker schemaSpellchecker settings. schemaTheme for decorating misspelt words, one of:
  - 'background-box': fills the background of the misspelt word;
  - 'wavy-underline': underline with wavelets (note: Chrome has a bug which prevents rendering of wavelets under some very short words)
  - 'dotted-underline': underline with dotted style Project-Id-Version: jupyterlab
PO-Revision-Date: 2021-08-17 18:06
Language-Team: Polish
Language: pl_PL
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=4; plural=(n==1 ? 0 : (n%10>=2 && n%10<=4) && (n%100<12 || n%100>14) ? 1 : n!=1 && (n%10>=0 && n%10<=1) || (n%10>=5 && n%10<=9) || (n%100>=12 && n%100<=14) ? 2 : 3);
X-Crowdin-File: /master/extensions/spellchecker/locale/spellchecker.pot
X-Crowdin-File-ID: 103
X-Crowdin-Language: pl
X-Crowdin-Project: jupyterlab
X-Crowdin-Project-ID: 409874
 %1 [%2] %1 [%2] (online) Popraw na Wybierz język sprawdzania pisowni Słownik nie jest załadowany Zignoruj Język sprawdzania pisowni Ładowanie słownika… Typy MIME dla plików/edytorów, dla których należy aktywować sprawdzanie pisowni Brak podpowiedzi Słowniki online Sprawdzanie pisowni Motyw Przełącz sprawdzanie pisowni Słowa do zignorowania przy sprawdzaniu pisowni Lista słowników online, które mają być używane, jeśli instalacja słowników w ścieżce danych jupyter-server jest niemożliwa lub niepożądana. Na przykład:

[
    {
        "id": "pl_PL-online",
        "aff": "http://some-url/pl_PL.aff",
        "dic": "http://some-url/pl_PL.dic",
        "name": "polski (Polska)"
    }
] Lista słów do zignorowania, uwzględniając wielkość liter Identyfikator słownika, np. en-us Lista typów MIME. GFM oznacza GitHub Flavored Markdown Sprawdzanie pisowni Ustawienia sprawdzania pisowni. Motyw do dekoracji błędnych słów, jeden z:
  - 'background-box': wypełnia tło nieprawidłowego słowa;
  - 'wavy-underline': podkreślenie falami (uwaga: Chrome ma błąd, który zapobiega renderowaniu fal pod bardzo krótkimi słowami)
  - 'dotted-underline': podkreślenie z kropkowanym stylem 
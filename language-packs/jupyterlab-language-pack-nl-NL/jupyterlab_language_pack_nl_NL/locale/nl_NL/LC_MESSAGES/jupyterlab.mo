��    s      �      L      L     M     c     o          �  
   �     �     �  %   �           /     P     h          �  "   �     �     �  &   	  $   2	  .   W	     �	  '   �	     �	  &   �	     
     
     3
  (   O
     x
      �
     �
     �
     �
     �
       7        N     k     x  !   �  /   �     �                ;     O     h     �     �     �  =   �       r     �   �     Z     u  0   �     �     �     �     �       +   %     Q     f  1   z     �  h   �     .     D     X     l       %   �     �     �     �  &     b  *  E   �     �  9   �  �         �     �     �  "        (     9  4   U  A   �  S   �  &      �   G  ^   �  ^   3  ,   �  l   �  `   ,     �     �  J   �  ,     ,   9  |   f  G   �  L   +  &   x  �   �  %   u  1   �     �     �  �  �     �     �     �     �     �     �  
   �     �          *     8     T     e     u     �     �     �     �  )   �               :  %   R     x  &   �     �     �     �  #   �          #  	   C     M     a     i     �  A   �     �     �     �           )      B       `      �      �      �      �      �      �      �   /   �      *!  �   ?!  �   �!     �"     �"  *   �"  
   �"     �"     �"  	   #  	   #  !   !#     C#     O#  1   [#     �#  d   �#     $  
   $  
   $  	   '$     1$      ?$     `$     u$     }$     �$  �  �$  F   3&  
   z&  5   �&  �   �&     V'     e'     z'     �'     �'     �'  )   �'  B   �'  F   8(     (  �   �(  h   -)  b   �)  #   �)  g   *  V   �*     �*     �*  @   +     B+     U+  s   h+  /   �+  :   ,     G,  �   e,     -     5-  
   Q-     \-   Reload Without Saving Save Failed Save and Reload menuOpen With menuText Editor Indentation menuTheme schemaApplication Commands schemaApplication Context Menu schemaApplication commands settings. schemaCommand Palette schemaCommand palette settings. schemaDocument Manager schemaDocument Search schemaDocument search plugin. schemaExtension Manager schemaExtension manager settings. schemaFile Browser schemaFile Browser Download schemaFile Browser Download settings. schemaFile Browser Open Browser Tab schemaFile Browser Open Browser Tab settings. schemaFile Browser Open With schemaFile Browser Open With settings. schemaFile Browser settings. schemaFile editor completer settings. schemaHelp schemaHelp settings. schemaJupyterHub settings. schemaJupyterLab context menu settings. schemaMarkdown Viewer schemaMarkdown viewer settings. schemaPrint schemaPrint settings. schemaSidebar schemaSidebar layout settings. schemaText Editor schemaText editor settings for all CodeMirror editors. schemaText editor settings. schemaTheme schemaTheme manager settings. settingsApplication Context Menu settingsApplication-level visual styling theme settingsAutosave Documents settingsAutosave Interval settingsCommand arguments settingsCommand id settingsDefault Viewers settingsDisclaimed Status settingsEditor settingsEditor Configuration settingsEnable CDN settingsEnable/disable styling of the application scrollbars settingsEnabled Status settingsEnables extension manager (requires Node.js/npm).
WARNING: installing untrusted extensions may be unsafe. settingsEnables using the CDN to fetch full package data.  Otherwise, the configured NPM registry will be used. Due to a lack of CORS support by NPM registry, only disable if supplying a custom registry settingsExtension Manager settingsFile Browser settingsFilter on file name with a fuzzy search settingsFont Family settingsFont Size settingsHide Front Matter settingsItem rank settingsItem type settingsLength of save interval in seconds settingsLine Height settingsLine Width settingsMargin for last modified timestamp check settingsMarkdown Viewer settingsMax acceptable difference, in milliseconds, between last modified timestamps on disk and client settingsMenu icon id settingsMenu items settingsMenu label settingsMenu rank settingsMenu unique id settingsMnemonic index for the label settingsModal Command Palette settingsNPM CDN settingsNPM Registry settingsNavigate to current directory settingsNote: To disable a context menu item,
copy it to User Preferences and add the
"disabled" key. The following example will disable Download item on files:
{
  "contextMenu": [
    {
      "command": "filebrowser:download",
      "selector": ".jp-DirListing-item[data-isdir=\"false\"]",
      "disabled": true
    }
  ]
}

Context menu description: settingsOverride theme CSS variables by setting key-value pairs here settingsOverrides settingsOverrides for the default viewers for file types settingsOverrides for where to show sidebar items
e.g., {"jp-debugger-sidebar": "left"}
You can also change this by right-clicking the sidebar icons. settingsRender Timeout settingsScrollbar Theming settingsShow hidden files settingsShow last modified column settingsSidebar settingsSubmenu definition settingsThe CSS selector for the context menu item. settingsThe URI of the CDN to use for fetching full package data settingsThe URI of the NPM registry to use for searching for jupyterlab extensions settingsThe application context menu. settingsThe configuration for all text editors.
If `fontFamily`, `fontSize` or `lineHeight` are `null`,
values from current theme are used. settingsThe font family used to render markdown.
If `null`, value from current theme is used. settingsThe line height used to render markdown.
If `null`, value from current theme is used. settingsThe render timeout in milliseconds. settingsThe size in pixel of the font used to render markdown.
If `null`, value from current theme is used. settingsThe text line width expressed in CSS ch units.
If `null`, lines fit the viewport width. settingsTheme CSS Overrides settingsTheme Manager settingsWhether the command palette should be modal or in the left panel. settingsWhether the item is disabled or not settingsWhether the menu is disabled or not settingsWhether the user understand that extensions managed through this interface run arbitrary code that may be dangerous settingsWhether to apply fuzzy algorithm while filtering on file names settingsWhether to automatically navigate to a document's current directory settingsWhether to autosave documents settingsWhether to hide YAML front matter.
The YAML front matter must be placed at the top of the document,
started by a line of three dashes (---) and ended by a line of
three dashes (---) or three points (...). settingsWhether to show hidden files settingsWhether to show the last modified column settingsfont-family settingsfont-size Project-Id-Version: jupyterlab
PO-Revision-Date: 2021-10-29 15:49
Language-Team: Dutch
Language: nl_NL
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=2; plural=(n != 1);
X-Crowdin-File: /master/jupyterlab/locale/jupyterlab.pot
X-Crowdin-File-ID: 93
X-Crowdin-Language: nl
X-Crowdin-Project: jupyterlab
X-Crowdin-Project-ID: 409874
 Herladen zonder op te slaan Opslaan is mislukt Opslaan & Herladen Open met Inspringing teksteditor Thema Commando's Toepassingscontextmenu Commando's en instellingen. Commandopalet Commandopalet instellingen. Documentenbeheer Document zoeken Document zoekplugin. Extensiebeheer Instellingen extensiebeheer. Bestandsbeheer Bestandsbeheer download Downloadinstellingen voor bestandsbeheer. Bestandsbeheer tab Bestandsbeheer tabinstellingen. Bestandsbeheer open met Bestandsbeheer open met instellingen. Instellingen bestandsbeheer. Bestandseditor completer instellingen. Help Help instellingen. JupyterHub instellingen. JupyterLab contextmenuinstellingen. Markdown weergave Markdown weergave instellingen. Afdrukken Afdrukinstellingen. Zijbalk Zijbalk lay-outinstellingen. Tekstbewerker Tekstbewerkingsinstellingen voor alle CodeMirror tekstverwerkers. Instellingen tekstbewerker. Thema Instellingen themabeheer. Toepassingscontextmenu Visuele stijl toepassing Bewaar documenten automatisch Interval van automatisch opslaan Argumenten commando Commando id Standaard weergaves Afgewezen Status Bewerker Configuratie tekstbewerker CDN inschakelen Stileren applicatie-scrollbalk in-/uitschakelen Ingeschakelde status Extensiebeheer inschakelen (Node.js/NPM vereist).
WAARSCHUWING: het installeren van niet-vertrouwde extensies kan onveilig zijn. Gebruik CDN om complete pakketdata op te halen.  Anders, de ingestelde NPM opslagplaats gebruiken. Wegens ontbreken CORS ondersteuning door de NPM opslagplaats, alleen uitschakelen indien de opslagplaats aangepast is Extensiebeheer Bestandsbeheer Filter bestandsnaam met fuzzy zoekopdracht Lettertype Lettergrootte Verberg inleiding Item rang Item type Lengte opslaginterval in seconden Regelhoogte Lijnbreedte Marge voor controle tijdstempel laatste wijziging Markdown weergave Max acceptabel verschil tussen laatst gewijzigde tijdstempels op schijf en cliënt, in milliseconden Menu icon id Menu items Menu label Menu rang Menu uniek id Mnemonische index voor het label Modaal commandopalet NPM CDN NPM opslagplaats Navigeer naar huidige map Opmerking: Om een contextmenu-item uit te schakelen,
kopieer het naar gebruikersinstellingen en voeg de
"uitgeschakeld" toets toe. Het volgende voorbeeld schakelt Download item in bestanden uit:
{
  "contextMenu": [
    {
      "command": "filebrowser:download",
      "selector": ". p-DirListing-item[data-isdir=\"false\"]",
      "uitgeschakeld": echte
    }
  ]
}

Context menu beschrijving: Overschrijf CSS variabelen door hier sleutelwaarde paren in te stellen Vervangers Vervangers voor standaardweergaves voor bestandstypen Vervangers voor positie zijbalkitems
b.v. {"jp-debugger-sidebar": "left"}
Je kunt dit ook veranderen door met de rechtermuisknop op de zijbalk te klikken. Render-timeout Scrollbalk stilering Verborgen bestanden tonen Toon kolom laatste wijziging Zijbalk Submenu definitie De CSS-selector voor het contextmenuitem. URI van de CDN die voor ophalen complete pakketdata gebruikt wordt URI van de CDN die voor zoeken naar Jupterlab extensies gebruikt wordt Toepassingscontextmenu. Configuratie voor alle tekstverwerkers.
Indien `fontFamily`, `fontSize` of `lineHeight` gelijk `null`,
worden waarden van het huidige thema gebruikt. Lettertype van Markdown weergave.
Indien `null` wordt de standaardwaarde van het huidige thema gebruikt. Regelhoogte Markdown tekst.
Indien `null` wordt de standaardwaarde van het huidige thema gebruikt. De render-timeout in milliseconden. Pixelgrootte van Markdown tekst.
Indien `null` wordt de standaardwaarde van het huidige thema gebruikt. Lijnbreedte tekst in ch CSS eenheden.
Indien `null` wordt de viewportbreedte gebruikt. Thema CSS vervangers Thema Beheerder Of het commando palet modaal of in het linker paneel staan moet. Item uitgeschakeld Menu uitgeschakeld Gebruiker begrijpt dat extensies beheerd door deze interface willekeurige, potentieel gevaarlijk code kan uitvoeren Gebruik fuzzy algoritme bij bestandsnaam filter Automatisch navigeren naar de huidige map van een document Bewaar documenten automatisch Verberg YAML inleiding.
De YAML inleiding moet bovenaan het document geplaatst worden,
beginnend met drie streepjes (---) en eindigend met drie streepjes (---) of drie punten (...). Verborgen bestanden tonen Toon kolom laatst wijziging lettertype lettergrootte 
<h1 align="center">SDDI CKAN Docker, Image SDDI-URBAN</h1>

 

Dieses Repository geht aus den Entwicklungen der Landeshauptstadt München (LHM) für das Förderprojekt
[„Connected Urban Twins“](https://www.connectedurbantwins.de) (CUT) hervor. Diese knüpfen an die Entwicklungen des Lehrstuhls für Geoinformatik der Technischen Universität München (TUM) im Bereich [Smart District Data Infrastructure](https://www.asg.ed.tum.de/en/gis/projects/smart-district-data-infrastructure/) (SDDI) an. Das Repository stellt ein [CKAN](https://github.com/ckan) Docker Image als Lösung für 
Metadatenkataloge urbaner digitaler Zwillinge zur Verfügung und kann in Kombination mit dem [`sddi-ckan-k8s`](https://github.com/tum-gis/sddi-ckan-k8s) 
Helm chart verwendet werden.
Das Image enthält CKAN selbst, kompiliert mit einem Satz an CKAN extensions 
und Anpassungen, um Funktionalität für das Konzept urbaner digitaler Zwillinge hinzuzufügen.


## :book: Inhaltsverzeichnis

- [:book: Inhaltsverzeichnis](#book-inhaltsverzeichnis)
- [:inbox\_tray: Varianten](#inbox_tray-varianten)
  - [`sddi-urban`](#sddi-urban)
- [:1234: Image Versionierung](#1234-image-versionierung)
  - [CKAN und CKAN Extension Versionen](#ckan-und-ckan-extension-versionen)
- [:rocket: Verwendung](#rocket-verwendung)
- [:book: Konfiguration und Dokumentation](#book-konfiguration-und-Dokumentation)
- [:hammer\_and\_wrench: Mitwirkung](#hammer_and_wrench-mitwirkung)
- [:handshake: Acknowledgement](handshake-acknowledgement)

## :inbox_tray: Varianten

Die CKAN-SDDI Docker-Images werden in verschiedenen Varianten veröffentlicht, siehe 
[SDDI-CKAN-K8s](https://github.com/tum-gis/sddi-ckan-k8s). Mit `sddi-urban` wird eine weitere Variante hinzugefügt.
Sie kann als [Package](https://github.com/orgs/it-at-m/packages?repo_name=ckan-docker) von diesem Repository 
heruntergeladen werden.

```bash
docker pull ghcr.io/it-at-m/ckan-sddi-urban

```

### `sddi-urban`

`sddi-base` + einige CKAN extensions für erweiterte Daten- und Ressource Vorschau sowie Optionen zur Beschreibung,
erweiterte Unterstützung für Import-/ Export, Harvesting und Sicherheit. Einige Extensions von `sddi-base`
sind installiert, aber deaktiviert. Diese können leicht wieder aktiviert werden, indem man sie über die Helm Chart Values
in die Plugin Liste in der CKAN Konfigurationsdatei integriert. Insgesamt sind folgende Plugins aktiviert: 

```yaml
plugins: >
  image_view text_view recline_view webpage_view
  scheming_datasets scheming_groups scheming_organizations
  spatial_metadata spatial_query spatial_harvest_metadata_api
  composite hierarchy_form lhm lhm_theme hierarchy_display
  resourcedictionary datastore xloader hierarchy_group_form
  password_policy resource_proxy geo_view geojson_view wmts_view shp_view
  harvest ckan_harvester csw_harvester waf_harvester doc_harvester
  gdpr iso keycloak noanonaccess clamav envvars
```

Diese Image beinhaltet außerdem ein etwas anderes Set and vorinstallierten SDDI Gruppen und Themen
well as the option of custom theming and custom metadata schemas, inspired by the requirements
sowie die Option einer angepassten graphischen Oberfläche und maßgeschneiderten Metadatenschemata,
inspiriert durch die Anforderungen der Landeshauptstadt München (LHM)

```text
ghcr.io/it-at-m/ckan-sddi-urban
```

## :1234: Image Versionierung

Die Images in diesem Repository sind versioniert und getagged nach den
[Releases](https://github.com/it-at-m/ckan-docker/releases) dieses Repositories.
Das `latest` Tag kennzeichnet den letzten produktiven Release.

Alle verfügbaren Tags sind in den packages jedes Images aufgelistet:

- [`sddi-urban`](https://github.com/it-at-m/ckan-docker/pkgs/container/ckan-sddi-urban)

### CKAN und CKAN Extension Versionen

CKAN version: `2.9.9`
CKAN base image: `ghcr.io/keitaroinc/ckan:2.9.9-focal`

Die CKAN-Katalogplattform verwendet mehrere Erweiterungen, um die für das SDDI-Konzept erforderliche Funktionalität 
bereitzustellen. Die folgende Tabelle listet die enthaltenen Erweiterungen mit der derzeit verwendeten Version auf. 
Je nach Version des upstream-Repositorys der einzelnen Erweiterungen bezieht sich die Version entweder auf eine 
*Release-Version* oder auf einen *Commit-Hash*.

Um eine stabile Versionierung der Images sicherzustellen, sind die Versionen in den `Dockerfiles` immer auf eine
stabile Versionsnummer oder einen Commit-Hash festgelegt.

> **Hinweis:** Die Versionsfestlegung wird nur für Release-Versionen angewendet.
> Weitere Entwicklungs-Images können stattdessen von upstream-Branches abhängen.


| Extension | Version | `sddi-base` | `sddi` | `sddi-social` | `sddi-urban` | Beschreibung |
|---|---|:---:|:---:|:---:|:---:|---|
| [`scheming`](https://github.com/MarijaKnezevic/ckanext-scheming), [`scheming (sddi-urban)`](https://github.com/gislab-augsburg/ckanext-scheming) | `f98daec`, `a7fdd9c`| :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | Konfiguration und teilen von CKAN Metadaten-Formularen. |
| [`hierarchy`](https://github.com/ckan/ckanext-hierarchy) | `v1.2.0` | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | Erlaubt es, Organisationen und Gruppen in hierarchisch zu organisieren (Obergruppen, Untergruppen und -Organisationen). |
| [`grouphierarchysddi`](https://github.com/tum-gis/ckanext-grouphierarchy-sddi) |  `1.1.3` | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |  | Erweitert `hierarchy` Mit vordefinierten Gruppen und Themen des SDDI-Konzepts. |
| [`relation`](https://github.com/tum-gis/ckanext-relation-sddi) | `1.0.3` | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |  | Macht es möglich, verschiedene Arten von Beziehungen (*realated_to*, *depends_on*, *part_of*) zwischen Katalogeinträgen zu erstellen und zu visualisieren. |
| [`spatial`](https://github.com/MarijaKnezevic/ckanext-spatial) | `c2118b9` | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | Bietet die Möglichkeit, über ihre räumliche Ausdehnung nach Datensätzen zu suchen. |
| [`datesearch`](https://github.com/MarijaKnezevic/ckanext-datesearch) | `1.0.2` | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |  | Bietet die Möglichkeit, nach Datensätzen entsprechend eines gegebenen Zeitrahmens zu suchen. Die Suche umfasst alle Datensätze, bei denen die Gültigkeitszeit mindestens eine Sekunde mit dem Suchzeitrahmen überschneidet. |
| [`repeating`](https://github.com/MarijaKnezevic/ckanext-repeating) | `1.0.0` | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |  | Diese Erweiterung bietet eine Möglichkeit, wiederkehrende Felder in CKAN-Datensätzen, -Ressourcen, -Organisationen und -Gruppen zu speichern. |
| [`composite`](https://github.com/EnviDat/ckanext-composite) | `1e6d7bb` | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | Die Erweiterung ermöglicht das Speichern strukturierter Metadaten für Datensätze, einzelne oder mehrere Felder. Die Unterfelder können einfacher Text, Datentyp oder Dropdown-Listen sein. |
| [`restricted`](https://github.com/MarijaKnezevic/ckanext-restricted) | `1.0.0` |  | :heavy_check_mark: | :heavy_check_mark: |  | CKAN-Erweiterung zur Einschränkung des Zugriffs auf die Ressourcen eines Datensatzes. So sind die Metadaten des Pakets zugänglich, jedoch nicht die Daten selbst (Ressource). Das Zugriffsrestriktion-Level für die Ressource kann individuell für jedes Paket definiert werden.  |
| [`dcat`](https://github.com/ckan/ckanext-dcat) | `v1.4.0` |  | :heavy_check_mark: | :heavy_check_mark: |  | Ermöglicht es CKAN, Metadaten aus anderen Katalogen zu exponieren und zu konsumieren, indem RDF-Dokumente verwendet werden, die mit DCAT serialisiert sind. |
| [`geoview`](https://github.com/ckan/ckanext-geoview) | `v0.0.20` |  | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | Diese Erweiterung enthält Ansichts-Plugins, um raumbezogene Dateien und Dienste (z.B. WMS) in CKAN anzuzeigen. |
| [`disqus`](https://github.com/ckan/ckanext-disqus) |  |  |  | :heavy_check_mark: |  | Die Disqus-Erweiterung ermöglicht es den Besuchern der Website, Kommentare zu einzelnen Paketen über ein AJAX-basiertes Kommentarsystem abzugeben. |
| [`password_policy`](https://github.com/keitaroinc/ckanext-password-policy) | `5618dc9`|:heavy_check_mark:  |:heavy_check_mark:| :heavy_check_mark: | :heavy_check_mark: | CKAN-Erweiterung, die eine Passwortrichtlinie für alle Benutzer hinzufügt. |
| [`resourcedictionary`](https://github.com/keitaroinc/ckanext-resourcedictionary) | `v1.0.0` |  |  |  | :heavy_check_mark: | Erweitert die Standardfunktionalität des CKAN Data Dictionary, indem die Möglichkeit hinzugefügt wird, ein Data Dictionary zu erstellen, bevor die tatsächlichen Daten in den Datenspeicher hochgeladen werden..  |
| [`xloader`](https://github.com/ckan/ckanext-xloader) | `1.0.1` |  |  |  | :heavy_check_mark: | Bietet eine schnellere und robustere Möglichkeit, Daten in CKANs DataStore zu laden. |
| [`lhm`](https://github.com/MandanaMoshref/ckanext-lhm) | `d28dbfa` |  |  |  | :heavy_check_mark: | Fügt Optionen für ein benutzerdefiniertes Metadaten-Schema, benutzerdefinierte Frontend-Gestaltung und ein angepasstes Set von Gruppen und Themen hinzu, inspiriert durch die Anforderungen an Datenkataloge für kommunale und städtische Digitale Zwillinge. |
| [`harvest`](https://github.com/ckan/ckanext-harvest) | `v1.5.6` |  |  |  | :heavy_check_mark: | Bietet ein Framework und Verwaltungstools für das automatische Harvesting anderer Metadatenkataloge. |
| [`glab`](https://github.com/gislab-augsburg/ckanext-glab/tree/gdpr) | `0612d22` |  |  |  | :heavy_check_mark: |  Fügt erweiterte Sicherheits- und Datenschutz-Funktionen hinzu. |
| [`iso`](https://github.com/gislab-augsburg/ckanext-iso) | `c4c28a8` |  |  |  | :heavy_check_mark: | Überarbeitung und Anpassung des CSW-Harvesters von ckanext-spatial an die Anforderungen für das Harvesting von Geoportalen mit ISO-19115 Metadaten.  |
| [`noanonaccess`](https://github.com/gislab-augsburg/ckanext-iso) | `v2.0.4` |  |  |  | :heavy_check_mark: | Bietet die Option, den Zugang zu einem Metadatenkatalog oder bestimmten Funktionen auf registrierte Benutzer zu beschränken. |
| [`keycloak`](https://github.com/gislab-augsburg/ckanext-keycloak) | `5859aec` |  |  |  | :heavy_check_mark: | Fügt Optionen für Single Sign-On hinzu und ermöglicht es Benutzern, sich mit Keycloak zu authentifizieren, anstatt ein neues Benutzerkonto zu erstellen. |
| [`clamav`](https://github.com/gislab-augsburg/ckanext-clamav) | `c483b5d` |  |  |  | :heavy_check_mark: | Scannt hochgeladene Ressourcen-Dateien auf Malware mit der ClamD-Library. |


## :rocket: Verwendung

Die in diesem Repository bereitgestellten Images sind für den [`sddi-ckan-k8s`](https://github.com/tum-gis/sddi-ckan-k8s) 
Helm-Chart konzipiert. Im Helm-Chart-Repository sind Beispiele zu finden, wie die Images ausgeführt werden können.

## :book: Konfiguration und Dokumentation

Die Konfiguration der Docker-Images erfolgt hauptsächlich über Umgebungsvariablen unter Verwendung der 
Namenskonvention von [`ckanext-envvars`](https://github.com/okfn/ckanext-envvars). Die verfügbaren Konfigurationsoptionen
sind in der Dokumentation von [`ckan`](https://docs.ckan.org/en/latest/maintaining/configuration.html) und in den
oben aufgeführten Erweiterungen zu finden.

## :handshake: Acknowledgement

Dieses Code-Entwicklungsprojekt wird maßgeblich durch das Förderprojekt
[„Connected Urban Twins“](https://www.connectedurbantwins.de) (CUT) unterstützt. CUT ist eines von 73 ausgewählten
Modellprojekten Smart Cities (MPSC) und wird im Rahmen des Förderprogramms
des Bundesministeriums für Wohnen, Stadtentwicklung und Bauwesen (BMWSB)
gefördert. Ziel des Projekts ist die Entwicklung und Nutzung urbaner
digitaler Zwillinge zur Förderung einer nachhaltigen und integrierten
Stadtentwicklung.


<p align="left" height="200" line-height="200">
  <a href="https://www.connectedurbantwins.de" target="_blank">
    <img src="https://www.connectedurbantwins.de/app/uploads/2022/08/logo.png"
    alt="TwinBy" height="100"/>
  </a>
</p>

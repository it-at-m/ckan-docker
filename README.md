<h1 align="center">SDDI CKAN Docker, Image SDDI-URBAN</h1>

 

Dieses Repository geht aus den Entwicklungen der Landeshauptstadt München (LHM) für das Förderprojekt
[„Connected Urban Twins“](https://www.connectedurbantwins.de) (CUT) hervor. Diese knüpfen an die Entwicklungen des Lehrstuhls für Geoinformatik der Technischen Universität München (TUM) im Bereich [Smart District Data Infrastructure](https://www.asg.ed.tum.de/en/gis/projects/smart-district-data-infrastructure/) (SDDI) an. Das Repository stellt ein [CKAN](https://github.com/ckan) Docker Image als Lösung für 
Metadatenkataloge urbaner digitaler Zwillinge zur Verfügung und kann in Kombination mit dem [`sddi-ckan-k8s`](https://github.com/tum-gis/sddi-ckan-k8s) 
Helm chart verwendet werden.
Das Image enthält CKAN selbst, kompiliert mit einem Satz an CKAN Extensions 
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
[tum-gis/ckan-docker](https://github.com/tum-gis/ckan-docker). Mit `sddi-urban` wird eine weitere Variante hinzugefügt.
Sie kann als [Package](https://github.com/orgs/it-at-m/packages?repo_name=ckan-docker) von diesem Repository 
heruntergeladen werden.

```bash
docker pull ghcr.io/it-at-m/ckan-sddi-urban

```

### `sddi-urban`

`sddi-base` + einige CKAN Extensions für erweiterte Daten- und Ressource Vorschau sowie Optionen zur Beschreibung,
erweiterte Unterstützung für Import-/ Export, Harvesting und Sicherheit. Nicht alle Plugins der installierten Extensions
sind aktiviert. Eine Anpassung der aktivierten Plugins kann über die Plugin-Liste im Dockerfile oder (bei Installation auf einer Containerplattform) 
über die Helm Chart Values angepasst werden. Nähere Informationen zu Exetnsions und deren Plugins finden sich in den unten verlinkten Repositories.
Initial sind folgende Plugins aktiviert:

```yaml
plugins: >
  activity image_view text_view datatables_view webpage_view
  scheming_nerf_index scheming_datasets scheming_groups scheming_organizations
  spatial_metadata spatial_query spatial_harvest_metadata_api
  composite hierarchy_form lhm lhm_theme hierarchy_display
  resourcedictionary datastore xloader hierarchy_group_form
  resource_proxy geo_view geojson_view wmts_view shp_view
  harvest ckan_harvester csw_harvester waf_harvester doc_harvester
  gdpr iso keycloak noanonaccess security clamav envvars
```

Diese Image beinhaltet außerdem ein etwas anderes Set an vorinstallierten SDDI Gruppen und Themen
sowie die Option einer angepassten graphischen Oberfläche sowie maßgeschneiderten Metadatenschemata
und ist an den Betrieb auf Container-Plattformen wie OpenShift angepasst, inspiriert durch die
Anforderungen der Landeshauptstadt München (LHM).

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

CKAN version: `2.11.2`
CKAN base image: `ckan/ckan-base:2.11.2`
TUM SDDI base image: `ghcr.io/tum-gis/ckan-sddi-base:3.1.1`

Die CKAN-Katalogplattform verwendet mehrere Erweiterungen, um die für das SDDI-Konzept erforderliche Funktionalität 
bereitzustellen. Die folgende Tabelle listet die enthaltenen Erweiterungen mit der derzeit verwendeten Version auf. 
Je nach Version des upstream-Repositorys der einzelnen Erweiterungen bezieht sich die Version entweder auf eine 
*Release-Version* oder auf einen *Commit-Hash*.

Um eine stabile Versionierung der Images sicherzustellen, sind die Versionen in den `Dockerfiles` immer auf eine
stabile Versionsnummer oder einen Commit-Hash festgelegt.

> **Hinweis:** Die Versionsfestlegung wird nur für Release-Versionen angewendet.
> Weitere Entwicklungs-Images können stattdessen von upstream-Branches abhängen.

| Extension | Version | `sddi-base` | `sddi-urban` | Beschreibung |
|---|---|:---:|:---:|:---|
| [`ckanext-hierarchy`](https://github.com/ckan/ckanext-hierarchy) | `v1.2.2` | :heavy_check_mark: | :heavy_check_mark: | Erlaubt es, Organisationen und Gruppen in hierarchisch zu organisieren (Obergruppen, Untergruppen und -Organisationen). |
| [`ckanext-scheming`](https://github.com/ckan/ckanext-scheming) | `27035f4` | :heavy_check_mark: | :heavy_check_mark: | Konfiguration und teilen von CKAN Metadaten-Formularen. |
| [`ckanext-geoview`](https://github.com/ckan/ckanext-geoview) | `v0.2.2` | :heavy_check_mark: | :heavy_check_mark: | Diese Erweiterung enthält Ansichts-Plugins, um raumbezogene Dateien und Dienste (z.B. WMS) in CKAN anzuzeigen. |
| [`ckanext-clamav (sddi-base)`](https://github.com/DataShades/ckanext-clamav), [`ckanext-clamav (sddi-urban)`](https://github.com/gislab-augsburg/ckanext-clamav) | `a1d23ac`, `c483b5d` | :heavy_check_mark: | :heavy_check_mark: | Scannt hochgeladene Ressourcen-Dateien auf Malware mit der ClamD-Library. |
| [`dcat`](https://github.com/ckan/ckanext-dcat) | `v1.5.1` | :heavy_check_mark: | :heavy_check_mark: | Ermöglicht es CKAN, Metadaten aus anderen Katalogen zu exponieren und zu konsumieren, indem RDF-Dokumente verwendet werden, die mit DCAT serialisiert sind. |
| [`ckanext-spatial`](https://github.com/ckan/ckanext-spatial) | `v2.3.1` |  | :heavy_check_mark: | Bietet die Möglichkeit, über ihre räumliche Ausdehnung nach Datensätzen zu suchen sowie Harvesting von ISO-19115 Metadaten via CSW-Schnittstelle |
| [`ckanext-resourcedictionary`](https://github.com/keitaroinc/ckanext-resourcedictionary) | `v1.0.0` |  | :heavy_check_mark: | Erweitert die Standardfunktionalität des CKAN Data Dictionary, indem die Möglichkeit hinzugefügt wird, ein Data Dictionary zu erstellen, bevor die tatsächlichen Daten in den Datenspeicher hochgeladen werden..  |
| [`ckanext-xloader`](https://github.com/ckan/ckanext-xloader) | `2.2.0` |  | :heavy_check_mark: | Bietet eine schnellere und robustere Möglichkeit, Daten in CKANs DataStore zu laden. |
| [`ckanext-lhm`](https://github.com/gislab-augsburg/ckanext-lhm) | `73030b6` |  | :heavy_check_mark: | Fügt Optionen für ein benutzerdefiniertes Metadaten-Schema, benutzerdefinierte Frontend-Gestaltung, ein angepasstes Set von Gruppen und Themen sowie angepasste Export- und Harvesting-Funktionen hinzu, inspiriert durch die Anforderungen der LHM an Datenkataloge für kommunale und städtische Digitale Zwillinge. |
| [`ckanext-harvest`](https://github.com/ckan/ckanext-harvest) | `v1.6.2` |  | :heavy_check_mark: | Bietet ein Framework und Verwaltungstools für das automatische Harvesting anderer Metadatenkataloge. |
| [`ckanext-glab`](https://github.com/gislab-augsburg/ckanext-glab/tree/gdpr) | `0612d22` |  | :heavy_check_mark: |  Fügt erweiterte Sicherheits- und Datenschutz-Funktionen hinzu. |
| [`ckanext-iso`](https://github.com/gislab-augsburg/ckanext-iso) | `9511a3a` |  | :heavy_check_mark: | Überarbeitung und Anpassung des CSW-Harvesters von ckanext-spatial an die Anforderungen der LHM für das Harvesting von ISO-19115 Metadaten via CSW-Schnittstelle.  |
| [`ckanext-keycloak`](https://github.com/gislab-augsburg/ckanext-keycloak) | `da6b273` |  | :heavy_check_mark: | Fügt Optionen für Single Sign-On hinzu und ermöglicht es Benutzern, sich automatisch mit Keycloak zu authentifizieren und einzuloggen. |
| [`ckanext-noanonaccess`](https://github.com/gislab-augsburg/ckanext-noanonaccess) | `290ca76` |  | :heavy_check_mark: | Bietet die Option, den Zugang zu einem Metadatenkatalog oder bestimmten Funktionen auf registrierte Benutzer zu beschränken. |
| [`ckanext-composite`](https://github.com/EnviDat/ckanext-composite) | `ea65c2a` |  | :heavy_check_mark: | Die Erweiterung ermöglicht das Speichern verschachtelter Metadaten mit Subfeldern für verschiedene Datentypen. |
| [`ckanext-security`](https://github.com/MarijaKnezevic/ckanext-security) | `0.0.1` |  | :heavy_check_mark: | Die Erweiterung beinhaltet eine Reihe von Verbesserungen der IT-Sicherheit für CKAN. |

## :rocket: Verwendung

Die in diesem Repository bereitgestellten Images sind für den [`sddi-ckan-k8s`](https://github.com/tum-gis/sddi-ckan-k8s) 
Helm-Chart konzipiert. Im Helm-Chart-Repository sind Beispiele zu finden, wie die Images ausgeführt werden können.

## :book: Konfiguration und Dokumentation

Die Konfiguration der Docker-Images erfolgt hauptsächlich über Umgebungsvariablen unter Verwendung der 
Namenskonvention von [`ckanext-envvars`](https://github.com/ckan/ckanext-envvars). Die verfügbaren Konfigurationsoptionen
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

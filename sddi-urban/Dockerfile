# ###############################################################################
# ## Build stage
# ##############################################################################
ARG BASEIMAGE_REPOSITORY=ghcr.io/tum-gis/ckan-sddi-base
ARG BASEIMAGE_VERSION=3.1.1
ARG CKAN_VERSION_BUILD_STAGE=2.11.2

FROM ckan/ckan-base:${CKAN_VERSION_BUILD_STAGE} as extbuild

USER root

RUN apt-get update && apt-get install -y \
    curl \
    libpq-dev \
    autoconf \
    automake \
    libtool \
    patch \
    musl-dev \
    libpcre3-dev \
    libpcre3 \
    libffi-dev \
    libxml2-dev \
    libxslt-dev

RUN pip install -U markupsafe==2.0.1 sqlalchemy==1.4.41

# ckanext-spatial #############################################################
ENV CKANEXT_SPATIAL_GITHUB_URL="https://github.com/ckan/ckanext-spatial"
ENV CKANEXT_SPATIAL_VERSION="v2.3.1"

RUN set -ex && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_SPATIAL_GITHUB_URL}.git@${CKANEXT_SPATIAL_VERSION}#egg=ckanext-spatial && \
  curl -o /wheels/ckanext-spatial-requirements.txt \
    https://raw.githubusercontent.com/ckan/ckanext-spatial/${CKANEXT_SPATIAL_VERSION}/requirements-py2.txt
  
# ckanext-resourcedictionary ##########################################################
ARG CKANEXT_RESOURCEDICTIONARY_VERSION="v1.0.0"
ENV CKANEXT_RESOURCEDICTIONARY_VERSION=${CKANEXT_RESOURCEDICTIONARY_VERSION}
ENV CKANEXT_RESOURCEDICTIONARY_GITHUB_URL="https://github.com/keitaroinc/ckanext-resourcedictionary"

RUN set -ex && \
  pip install -r \
    https://raw.githubusercontent.com/keitaroinc/ckanext-resourcedictionary/${CKANEXT_RESOURCEDICTIONARY_VERSION}/requirements.txt && \
  curl -o /wheels/ckanext-resourcedictionary.txt \
    https://raw.githubusercontent.com/keitaroinc/ckanext-resourcedictionary/${CKANEXT_RESOURCEDICTIONARY_VERSION}/requirements.txt && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_RESOURCEDICTIONARY_GITHUB_URL}.git@${CKANEXT_RESOURCEDICTIONARY_VERSION}#egg=ckanext-resourcedictionary

# ckanext-xloader ##########################################################
ARG CKANEXT_XLOADER_VERSION="2.1.0"
ENV CKANEXT_XLOADER_VERSION=${CKANEXT_XLOADER_VERSION}
ENV CKANEXT_XLOADER_GITHUB_URL="https://github.com/ckan/ckanext-xloader"

RUN set -ex && \
  #mkdir /wheels && \
  pip install -r \
    https://raw.githubusercontent.com/ckan/ckanext-xloader/${CKANEXT_XLOADER_VERSION}/requirements.txt && \
  curl -o /wheels/ckanext-xloader.txt \
    https://raw.githubusercontent.com/ckan/ckanext-xloader/${CKANEXT_XLOADER_VERSION}/requirements.txt && \
  pip install -U requests[security] && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_XLOADER_GITHUB_URL}.git@${CKANEXT_XLOADER_VERSION}#egg=ckanext-xloader

# ckanext-lhm ##########################################################
ARG CKANEXT_LHM_VERSION="54460a1"
ENV CKANEXT_LHM_VERSION=${CKANEXT_LHM_VERSION}
ENV CKANEXT_LHM_GITHUB_URL="https://github.com/gislab-augsburg/ckanext-lhm"

RUN set -ex && \
  pip install -r \
    https://raw.githubusercontent.com/gislab-augsburg/ckanext-lhm/${CKANEXT_LHM_VERSION}/requirements.txt && \
  curl -o /wheels/ckanext-lhm.txt \
    https://raw.githubusercontent.com/gislab-augsburg/ckanext-lhm/${CKANEXT_LHM_VERSION}/requirements.txt && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_LHM_GITHUB_URL}.git@${CKANEXT_LHM_VERSION}#egg=ckanext-lhm

# ckanext-harvest ##########################################################
ARG CKANEXT_HARVEST_VERSION="v1.6.2"
ENV CKANEXT_HARVEST_VERSION=${CKANEXT_HARVEST_VERSION}
ENV CKANEXT_HARVEST_GITHUB_URL="https://github.com/ckan/ckanext-harvest"

RUN set -ex && \
  pip install -r \
    https://raw.githubusercontent.com/ckan/ckanext-harvest/${CKANEXT_HARVEST_VERSION}/requirements.txt && \
  curl -o /wheels/ckanext-harvest.txt \
    https://raw.githubusercontent.com/ckan/ckanext-harvest/${CKANEXT_HARVEST_VERSION}/requirements.txt && \
  pip install -r \
    https://raw.githubusercontent.com/ckan/ckanext-harvest/${CKANEXT_HARVEST_VERSION}/dev-requirements.txt && \
  curl -o /wheels/ckanext-harvest-dev.txt \
    https://raw.githubusercontent.com/ckan/ckanext-harvest/${CKANEXT_HARVEST_VERSION}/dev-requirements.txt && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_HARVEST_GITHUB_URL}.git@${CKANEXT_HARVEST_VERSION}#egg=ckanext-harvest

## ckanext-scheming ##########################################################
#ARG CKANEXT_SCHEMING_VERSION="85eea67"
#ENV CKANEXT_SCHEMING_VERSION=${CKANEXT_SCHEMING_VERSION}
#ENV CKANEXT_SCHEMING_GITHUB_URL="https://github.com/ckan/ckanext-scheming"
#
#RUN set -ex && \
#  pip wheel --wheel-dir=/wheels \
#    git+${CKANEXT_SCHEMING_GITHUB_URL}.git@${CKANEXT_SCHEMING_VERSION}#egg=ckanext-scheming

# ckanext-glab ##########################################################
ARG CKANEXT_GLAB_VERSION="0612d22"
ENV CKANEXT_GLAB_VERSION=${CKANEXT_GLAB_VERSION}
ENV CKANEXT_GLAB_GITHUB_URL="https://github.com/gislab-augsburg/ckanext-glab"

RUN set -ex && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_GLAB_GITHUB_URL}.git@${CKANEXT_GLAB_VERSION}#egg=ckanext-glab

# ckanext-iso ##########################################################
ARG CKANEXT_ISO_VERSION="9511a3a"
ENV CKANEXT_ISO_VERSION=${CKANEXT_ISO_VERSION}
ENV CKANEXT_ISO_GITHUB_URL="https://github.com/gislab-augsburg/ckanext-iso"

RUN set -ex && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_ISO_GITHUB_URL}.git@${CKANEXT_ISO_VERSION}#egg=ckanext-iso

# ckanext-keycloak ##########################################################
ARG CKANEXT_KEYCLOAK_VERSION="5859aec"
ENV CKANEXT_KEYCLOAK_VERSION=${CKANEXT_KEYCLOAK_VERSION}
ENV CKANEXT_KEYCLOAK_GITHUB_URL="https://github.com/gislab-augsburg/ckanext-keycloak"

RUN set -ex && \
  pip install -r \
    https://raw.githubusercontent.com/gislab-augsburg/ckanext-keycloak/${CKANEXT_KEYCLOAK_VERSION}/requirements.txt && \
  curl -o /wheels/ckanext-keycloak.txt \
    https://raw.githubusercontent.com/gislab-augsburg/ckanext-keycloak/${CKANEXT_KEYCLOAK_VERSION}/requirements.txt && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_KEYCLOAK_GITHUB_URL}.git@${CKANEXT_KEYCLOAK_VERSION}#egg=ckanext-keycloak

# ckanext-noanonaccess ##########################################################
ARG CKANEXT_NOANONACCESS_VERSION="fa89e02"
ENV CKANEXT_NOANONACCESS_VERSION=${CKANEXT_NOANONACCESS_VERSION}
ENV CKANEXT_NOANONACCESS_GITHUB_URL="https://github.com/gislab-augsburg/ckanext-noanonaccess"

RUN set -ex && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_NOANONACCESS_GITHUB_URL}.git@${CKANEXT_NOANONACCESS_VERSION}#egg=ckanext-noanonaccess

# ckanext-clamav ##############################################################
ARG CKANEXT_CALMAV_VERSION="c483b5d"
ENV CKANEXT_CALMAV_VERSION=${CKANEXT_CALMAV_VERSION}
ENV CKANEXT_CALMAV_GITHUB_URL="https://github.com/gislab-augsburg/ckanext-clamav"

RUN set -ex && \
  pip wheel --wheel-dir=/wheels -r \
    https://raw.githubusercontent.com/mutantsan/ckanext-clamav/${CKANEXT_CALMAV_VERSION}/requirements.txt && \
  curl -o /wheels/ckanext-clamav.txt \
    https://raw.githubusercontent.com/mutantsan/ckanext-clamav/${CKANEXT_CALMAV_VERSION}/requirements.txt && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_CALMAV_GITHUB_URL}.git@${CKANEXT_CALMAV_VERSION}#egg=ckanext-clamav

## ckanext-composite ###########################################################
ARG CKANEXT_COMPOSITE_VERSION="1e6d7bb"
ENV CKANEXT_COMPOSITE_VERSION=${CKANEXT_COMPOSITE_VERSION}
ENV CKANEXT_COMPOSITE_GITHUB_URL="https://github.com/EnviDat/ckanext-composite"

RUN set -ex && \
  #pip install -r \
    #https://raw.githubusercontent.com/EnviDat/ckanext-composite/${CKANEXT_COMPOSITE_VERSION}/dev-requirements.txt && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_COMPOSITE_GITHUB_URL}.git@${CKANEXT_COMPOSITE_VERSION}#egg=ckanext-composite

# ckanext-password-policy #####################################################
#ARG CKANEXT_PASSWORD_POLICY_VERSION="5618dc9"
#ENV CKANEXT_PASSWORD_POLICY_VERSION=${CKANEXT_PASSWORD_POLICY_VERSION}
#ENV CKANEXT_PASSWORD_POLICY_GITHUB_URL="https://github.com/keitaroinc/ckanext-password-policy"
#
#RUN set -ex && \
#  pip install -r \
#    https://raw.githubusercontent.com/keitaroinc/ckanext-password-policy/${CKANEXT_PASSWORD_POLICY_VERSION}/requirements.txt && \
#  curl -o /wheels/ckanext-password-policy.txt \
#    https://raw.githubusercontent.com/keitaroinc/ckanext-password-policy/${CKANEXT_PASSWORD_POLICY_VERSION}/requirements.txt && \
#  pip wheel --wheel-dir=/wheels \
#    git+${CKANEXT_PASSWORD_POLICY_GITHUB_URL}.git@${CKANEXT_PASSWORD_POLICY_VERSION}#egg=ckanext-password-policy


# #############################################################################
# # Runtime stage
# #############################################################################
FROM ${BASEIMAGE_REPOSITORY}:${BASEIMAGE_VERSION} AS runtime

ENV CKAN_DIR=${SRC_DIR}/ckan
ENV DATA_DIR=/srv/app/data
ENV UWSGI_HARAKIRI=50

USER root

# Setting the locale
ENV LC_ALL="en_US.UTF-8"
RUN update-locale LANG=${LC_ALL}

# Cleanup to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Get artifacts from build stages
COPY --from=extbuild /wheels ${APP_DIR}/ext_wheels

RUN chown -R ckan:ckan-sys ${APP_DIR}

# Add CKAN dev tools (has an older toolbar pin)
ADD https://raw.githubusercontent.com/ckan/ckan/ckan-2.11.2/dev-requirements.txt /dev-requirements.txt
RUN pip install -r /dev-requirements.txt \
 && pip install --no-cache-dir "flask-debugtoolbar>=0.16.0,<1.0.0"
# optional: your SQLAlchemy panel helper
RUN pip install 'ckanext-fdt-sqlalchemy[deps]'

USER ckan

WORKDIR ${CKAN_DIR}

# ckanext-spatial #############################################################
RUN set -ex && \
  pip install -e 'git+https://github.com/ckan/ckanext-spatial.git#egg=ckanext-spatial' && \
  pip install -r 'https://raw.githubusercontent.com/ckan/ckanext-spatial/master/requirements.txt'

# ckanext-resourcedictionary ##################################################
RUN set -ex && \
  pip install -r ${APP_DIR}/ext_wheels/ckanext-resourcedictionary.txt && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-resourcedictionary

# ckanext-xloader #############################################################
RUN set -ex && \
  pip install -r ${APP_DIR}/ext_wheels/ckanext-xloader.txt && \
  pip install -U requests[security] && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-xloader
  
# ckanext-lhm #################################################################
RUN set -ex && \
  pip install -r ${APP_DIR}/ext_wheels/ckanext-lhm.txt && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-lhm

# ckanext-harvest #############################################################
RUN set -ex && \
  pip install -r ${APP_DIR}/ext_wheels/ckanext-harvest.txt && \
  pip install -r ${APP_DIR}/ext_wheels/ckanext-harvest-dev.txt && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-harvest

## ckanext-scheming #############################################################
## uninstall previous version from sddi-base
#RUN yes | pip uninstall ckanext-scheming
#RUN set -ex && \
#  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-scheming

# ckanext-glab #############################################################
RUN set -ex && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-glab

# ckanext-iso #############################################################
RUN set -ex && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-iso

## ckanext-keycloak #################################################################
RUN set -ex && \
  pip install -r ${APP_DIR}/ext_wheels/ckanext-keycloak.txt && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-keycloak

# ckanext-noanonaccess #############################################################
RUN set -ex && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-noanonaccess

# ckanext-clamav ##############################################################
# uninstall previous version from sddi-base
RUN yes | pip uninstall ckanext-clamav
RUN set -ex && \
  pip install -r ${APP_DIR}/ext_wheels/ckanext-clamav.txt && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-clamav

## ckanext-composite ###########################################################
RUN set -ex && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-composite

# ckanext-password-policy #####################################################
#RUN set -ex && \
#  pip install -r ${APP_DIR}/ext_wheels/ckanext-password-policy.txt && \
#  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-password-policy

# for password_policy ckan 2.11
#RUN set -ex && \
#  pip install repoze.who-friendlyform

ENV CKAN__PLUGINS "image_view text_view datatables_view webpage_view \
    scheming_datasets scheming_groups scheming_organizations \
    spatial_metadata spatial_query spatial_harvest_metadata_api \
    composite hierarchy_form lhm lhm_theme hierarchy_display \
    resourcedictionary datastore xloader hierarchy_group_form \
    resource_proxy geo_view geojson_view wmts_view shp_view \
    harvest ckan_harvester csw_harvester waf_harvester doc_harvester\
    gdpr iso keycloak noanonaccess clamav envvars"

# No config generation because we use local-ini via ConfigMap
#RUN set -ex && \
#  ckan generate config ${CKAN_INI}

# Create data dir, in CAP done by extra Volume
# Not necessary (?) because we use create it via PVC 
#RUN mkdir /srv/app/data

# install supervisor (old, as root) ########################################################
#RUN set -ex && \
#  apt-get update && \
#  apt-get -y install supervisor
#COPY supervisor/supervisor-ckan-worker.conf /etc/supervisor/conf.d
#COPY supervisor/supervisord.conf /etc/supervisor
#COPY supervisor/start-supervisor.sh /srv/app/docker-afterinit.d

RUN set -ex && \
  ckan config-tool "${CKAN_INI}" "ckan.plugins = ${CKAN__PLUGINS}" && \
  ckan config-tool "${CKAN_INI}" "ckanext.spatial.use_postgis_sorting = true" && \
  ckan config-tool "${CKAN_INI}" "ckanext.dcat.enable_content_negotiation = true" && \
  ckan config-tool "${CKAN_INI}" "ckan.default.package_type = dataset"

# Enable debug + templates + (optionally) keep Profiler enabled
#RUN ckan config-tool "${CKAN_INI}" \
  #"debug = true" \
  #"ckan.debug_templates = true"
  #"DEBUG_TB_ENABLED = false" \
  #"DEBUG_TB_INTERCEPT_REDIRECTS = false"

# Remove wheels
RUN set -ex && \
  rm -rf ${APP_DIR}/ext_wheels && \
  # Remove init script
  rm -f ${APP_DIR}/docker-afterinit.d/01_create_groups.sh

# Change user
USER root

# install supervisor ########################################################
RUN set -ex && \
  apt-get update && \
  apt-get -y install supervisor
COPY supervisor/supervisor-ckan-worker.conf /etc/supervisor/conf.d
COPY supervisor/supervisord.conf /etc/supervisor
#COPY supervisor/start-supervisor.sh /srv/app/docker-afterinit.d

# Set timezone
ENV TZ="Europe/Berlin"
RUN echo "${TZ}" > /etc/timezone

## Add debug capabilities
#ADD https://raw.githubusercontent.com/ckan/ckan/ckan-2.9.9/dev-requirements.txt /dev-requirements.txt
#RUN set -ex && \
#  pip install -r /dev-requirements.txt && \
#  rm /dev-requirements.txt && \
#  pip install 'ckanext-fdt-sqlalchemy[deps]'

# Download button
# Install pandas for get_data.py, libreoffice for PDF generation
# commented out libreoffice for development only because of long installation duration
RUN pip install pandas
#RUN yes | apt install libreoffice

# Change permissions recursively for all files in the local folders ? Needed?
RUN chmod -R 777 /srv/app/.local
RUN chmod -R 777 /usr/local

# Change user
USER ckan

# change ckan startscript for taking uwsgi worker number from uwsgi configMap
COPY startscript/start_ckan.sh /srv/app/start_ckan.sh

# TMP: Copy changed add_dataset buttons
COPY tmp/add_dataset.html /srv/app/src/ckan/ckan/templates/snippets/add_dataset.html

# TMP: Change resourcedictionary fields to required
COPY tmp/create.py /usr/local/lib/python3.8/dist-packages/ckanext/resourcedictionary/logic/action/create.py

# download button, user ckan
RUN mkdir /srv/app/md_download
COPY tmp/template_v1.2.2.xlsx /srv/app/md_download/template_v1.2.2.xlsx
COPY tmp/config-download.json /srv/app/md_download/config-download.json

## Not sure if thefollowing are needed: #############

WORKDIR ${APP_DIR}

# Create entrypoint directory for children image scripts
ONBUILD RUN mkdir -p /docker-entrypoint.d

# Supervisor start
COPY supervisor/start-supervisor.sh /docker-entrypoint.d/start-supervisor.sh

EXPOSE 5000
HEALTHCHECK --interval=60s --timeout=5s --retries=5 CMD curl --fail http://localhost:5000/api/3/action/status_show || exit CMD ["/srv/app/start_ckan.sh"]


CMD ["/srv/app/start_ckan.sh"]

###################################################

# TMP remaining changes in ckanext-lhm for upgrade
COPY theme_templates_2.11_groups_match /srv/app/.local/lib/python3.10/site-packages/ckanext/lhm/theme_templates_2.9.9


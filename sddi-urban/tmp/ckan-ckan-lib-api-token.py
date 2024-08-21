# -*- coding: utf-8 -*-

import jwt
import logging

from calendar import timegm

import ckan.plugins as plugins
import ckan.model as model
from ckan.common import config
from ckan.logic.schema import default_create_api_token_schema
from ckan.exceptions import CkanConfigurationException


log = logging.getLogger(__name__)

_config_encode_secret = u"api_token.jwt.encode.secret"
_config_decode_secret = u"api_token.jwt.decode.secret"
_config_secret_fallback = u"beaker.session.secret"

_config_algorithm = u"api_token.jwt.algorithm"


def _get_plugins():
    log.error("MB_DEBUG_01: ## def _get_plugins():")
    log.error("MB_DEBUG_01: plugins.PluginImplementations(plugins.IApiToken)")
    log.error(plugins.PluginImplementations(plugins.IApiToken))
    return plugins.PluginImplementations(plugins.IApiToken)


def _get_algorithm():
    log.error("MB_DEBUG_02: ## def get_algorithm():")
    log.error("MB_DEBUG_02: config.get(_config_algorithm)")
    log.error(config.get(_config_algorithm))
    return config.get(_config_algorithm, u"HS256")


def _get_secret(encode):
    log.error("MB_DEBUG_03: ## def _get_secret(encode):")
    log.error("MB_DEBUG_03: _config_decode_secret")
    log.error(_config_decode_secret)
    config_key = _config_encode_secret if encode else _config_decode_secret
    log.error("MB_DEBUG_03: _config_key")
    log.error(config_key)
    secret = config.get(config_key)
    log.error("MB_DEBUG_03: secret")
    log.error(secret)
    if not secret:
        secret = u"string:" + config.get(_config_secret_fallback, u"")
    type_, value = secret.split(u":", 1)
    log.error("MB_DEBUG_03: type_")
    log.error(type_)
    log.error("MB_DEBUG_03: value")
    log.error(value)
    if type_ == u"file":
        with open(value, u"rb") as key_file:
            value = key_file.read()
    if not value:
        raise CkanConfigurationException(
            (
                u"Neither `{key}` nor `{fallback}` specified. "
                u"Missing secret key is a critical security issue."
            ).format(
                key=config_key, fallback=_config_secret_fallback,
            )
        )
    return value


def into_seconds(dt):
    log.error("MB_DEBUG_04: ## def into_seconds(dt):")
    return timegm(dt.timetuple())


def get_schema():
    log.error("MB_DEBUG_05: ## def get_schema():")
    schema = default_create_api_token_schema()
    for plugin in _get_plugins():
        schema = plugin.create_api_token_schema(schema)
    return schema


def postprocess(data, jti, data_dict):
    log.error("MB_DEBUG_06: ## def postprocess(data, jti, data_dict):")
    for plugin in _get_plugins():
        data = plugin.postprocess_api_token(data, jti, data_dict)
    return data


def decode(encoded, **kwargs):
    encoded = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJBUmFWTmZNRC1jd2hjcEtEMGtXdzk3bjZHaGtkZVBJOVRpYXVMZFZOUkY3NHhLLS1EZnYxNFhSSjhfUW5tNGNqUWRKNVNMM2J4LVhRMHRSV0JIdjVOdyIsImlhdCI6MTcyNDIyNTQ5OX0.ygJMwLmxq0C5ImIswjPjAIqy-I-2EDFnkPsYrvCuIDU"
    log.error("MB_DEBUG_07: ## def decode(encoded, **kwargs):")
    log.error("MB_DEBUG_07: encoded")
    log.error(encoded)    
    log.error("MB_DEBUG_07: **kwargs -> is printed")
    print(**kwargs) 
    for plugin in _get_plugins():
        log.error("MB_DEBUG_07: plugin:")
        log.error(plugin)
        data = plugin.decode_api_token(encoded, **kwargs)
        log.error("MB_DEBUG_07: if data, log.error(data)")
        if data:
            log.error(data)
            break
    else:
        try:
            log.error("MB_DEBUG_07: _get_secret(encode=False)")
            log.error(_get_secret(encode=False))
            log.error("MB_DEBUG_07: _get_algorithm()")
            log.error(_get_algorithm())
            data = jwt.decode(
                encoded,
                _get_secret(encode=False),
                algorithms=_get_algorithm(),
                **kwargs
            )
        except jwt.InvalidTokenError as e:
            # TODO: add signal for performing extra work, like removing
            # expired tokens
            log.error(u"Cannot decode JWT token: %s", e)
            data = None
    log.error("MB_DEBUG_07: data")
    log.error(data)
    log.error("------------------------------------------")
    return data

##
def encode(data, **kwargs):
    log.error("MB_DEBUG_08: ## def encode(data, **kwargs):")
    log.error("MB_DEBUG_08: data")
    log.error(data)
    log.error("MB_DEBUG_08: **kwargs -> printed")
    print(**kwargs)
    for plugin in _get_plugins():
        token = plugin.encode_api_token(data, **kwargs)
        if token:
            log.error("MB_DEBUG_08: token-1")
            log.error(token)
            break
    else:
        token = jwt.encode(
            data,
            _get_secret(encode=True),
            algorithm=_get_algorithm(),
            **kwargs
        )
        log.error("MB_DEBUG_08: token-2")
        log.error(token)

    return token


def add_extra(result):
    log.error("MB_DEBUG_09: ## def add_extra(result):")
    for plugin in _get_plugins():
        result = plugin.add_extra_fields(result)
    return result


def get_user_from_token(token, update_access_time=True):
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJBUmFWTmZNRC1jd2hjcEtEMGtXdzk3bjZHaGtkZVBJOVRpYXVMZFZOUkY3NHhLLS1EZnYxNFhSSjhfUW5tNGNqUWRKNVNMM2J4LVhRMHRSV0JIdjVOdyIsImlhdCI6MTcyNDIyNTQ5OX0.ygJMwLmxq0C5ImIswjPjAIqy-I-2EDFnkPsYrvCuIDU"
    log.error("MB_DEBUG_10: ## def get_user_from_token(token, update_access_time=True):")
    log.error("MB_DEBUG_10: token:")
    log.error(token)
    data = decode(token)
    log.error("MB_DEBUG_10: data:")
    log.error(data)
    if not data:
        return
    # do preprocessing in reverse order, allowing onion-like
    # "unwrapping" of the data, added during postprocessing, when
    # token was created
    for plugin in reversed(list(_get_plugins())):
        data = plugin.preprocess_api_token(data)
    if not data or u"jti" not in data:
        return
    token_obj = model.ApiToken.get(data[u"jti"])
    log.error("MB_DEBUG_10: token_obj:")
    log.error(token_obj)
    if not token_obj:
        return
    if update_access_time:
        token_obj.touch(True)
    log.error("MB_DEBUG_10: token_obj.owner:")
    log.error(token_obj.owner)
    return token_obj.owner
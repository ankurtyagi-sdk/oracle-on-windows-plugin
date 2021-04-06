from utils import setupLogger, executeScript
from generated.definitions import RepositoryDefinition, SourceConfigDefinition
import json

def vdb_start (virtual_connection,parameters,repository,source_config):
    logger = setupLogger._setup_logger(__name__)

    env = {
            "DLPX_TOOLKIT_NAME" : "Oracle on Windows",
            "DLPX_TOOLKIT_WORKFLOW" : "vdb_start",
            "DLPX_TOOLKIT_PATH" : repository.delphix_tookit_path,
            "ORACLE_HOME" : repository.ora_home,
            "ORACLE_BASE" : repository.ora_base,
            "ORACLE_INST" : parameters.instance_name,
            "ORACLE_USER" : parameters.username,
            "ORACLE_PASSWD" : parameters.password,
            "VDB_MNT_PATH" : parameters.mount_path,
            "ORA_UNQ_NAME" : parameters.dbunique_name,
            "ORA_DB_NAME" : parameters.db_name
           }

    logger.debug("Virtual Parameters: {}".format(parameters))
    logger.debug("Virtual Repository Parameters: {}".format(repository))
    logger.debug("Source Config Parameters: {}".format(source_config))

    start_vdb =  executeScript.execute_powershell(virtual_connection,'vdb_start.ps1',env)
    logger.debug("Start VDB: {}".format(start_vdb))

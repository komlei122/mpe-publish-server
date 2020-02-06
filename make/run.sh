#!/usr/bin/env bash

cur=`dirname "$0"`

PJ_HOME=`cd "$cur/../"; pwd -P`

cd ${PJ_HOME}

# ---- pj_setting
DOCS_PATH=${PJ_HOME}/docs
SITES_DIR=${PJ_HOME}/release/books
BIN_DIR=${PJ_HOME}/make
CORE_PARSE_SCRIPT="${BIN_DIR}/mume_parse.js"

# ---- env_setting
NDOE_CMD="/usr/local/bin/node"

if [ ! -d ${SITES_DIR} ];then
  mkdir ${SITES_DIR}
else
  # clean
  rm -rf ${SITES_DIR}/*
  echo "clean ${SITES_DIR} done."
fi

cd ${BIN_DIR}

# copy 拷贝docs下的文件并生成index.md
echo "python build_index.py ${DOCS_PATH} ${SITES_DIR}"
python build_index.py ${DOCS_PATH} ${SITES_DIR}
echo "copy ${DOCS_PATH} to ${SITES_DIR} and build index done."

# build 开始编译所有markdown成为html文件
echo "python build_core.py "${SITES_DIR}" "${CORE_PARSE_SCRIPT}" "${NDOE_CMD}""
python build_core.py "${SITES_DIR}" "${CORE_PARSE_SCRIPT}" "${NDOE_CMD}"
echo "build_core parse markdown done."

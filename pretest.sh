#!/bin/bash

PRETEST_DIR=pretest-cloud
BUILD_CMD=./test.sh
TEST_CMD=./test.sh

HERE=$PWD

#verify repository present
git branch || exit 1

BRANCH=`git branch | grep "^*" | cut -d " " -f 2`
pushd /tmp
rm -rf $PRETEST_DIR
git clone $HERE $PRETEST_DIR || exit 1
cd $PRETEST_DIR
git checkout $BRANCH
$BUILD_CMD || exit 1
$TEST_CMD && echo '---SUCCESS'

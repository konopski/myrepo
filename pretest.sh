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
git clone $PRETEST_DIR || exit 1
cd $PRETEST_DIR
git checkout $BRANCH
$BUILD_CMD || exit 1
$TEST_CMD
RESULT=$?
if [ $RESULT ]
then
    echo '---SUCCESS'
else
    echo '---FAILED'
fi
exit $RESULT

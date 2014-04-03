#!/bin/bash

grep fork README.md ||  { echo "---ERROR: tests failure" ; exit 1;  }


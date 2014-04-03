#!/bin/bash

grep fork README.md ||  { echo "---ERROR: tests failure" ; exit 1;  }
grep next README.md ||  { echo "---ERROR: tests failure" ; exit 1;  }


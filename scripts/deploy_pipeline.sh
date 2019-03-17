#!/usr/bin/env bash

./build/install/late-samples-state/bin/late-samples-state --runner=DataflowRunner \
--project="staging-eabb77f6" --topic="projects/staging-eabb77f6/topics/late-samples-state-test" \
--jobName="late-samples-state-test" --workerMachineType="n1-standard-1"
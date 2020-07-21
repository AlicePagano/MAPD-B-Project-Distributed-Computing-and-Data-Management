#!/bin/bash
mkdir -p data/papers_in_json_singleline
cd data/papers_in_json
for filename in *.json; do
	echo $filename
	jq -c . $filename > ../papers_in_json_singleline/$filename
done
cd -

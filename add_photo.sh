#!/bin/sh
max=80
for ((i=1; i <= $max; i++)); do
    curl -X POST https://westcentralus.api.cognitive.microsoft.com/face/v1.0/persongroups/8131/persons/6f7ca34d-bd3c-43f8-950b-32b4514e043b/persistedFaces \
         -H 'Content-Type: application/octet-stream' \
         -H 'Ocp-Apim-Subscription-Key: b2670446099e461eb1e4ade6da59ac62' \
         --data-binary "@./sosuke/$i.jpg"
         echo "\n"
done


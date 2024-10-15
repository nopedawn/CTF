#!/bin/bash

# strings 070410aac49c772500581882f12a7a39f9ec6a662be52197f0c5d005390f251d

base64_parts=("VENQMVB7"
              "ODNmZTAz"
              "NGIyY2Zi"
              "MDlkZWFm"
              "YmI5NTVi"
              "MDMzOTJh"
              "MDgzZDhm"
              "ODNiMn0K")

full_string=""

for part in "${base64_parts[@]}"; do
    full_string+="$part"
done

echo "$full_string" | base64 -d


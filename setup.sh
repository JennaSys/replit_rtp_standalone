echo
echo "Installing Python 3.9..."
install-pkg python3.9

echo
echo "Installing Python dependencies..."
poetry install

# echo
# echo "Installing JavaScript dependencies..."
# npm install

# echo
# echo "Patching Transcrypt Parcel Plugin..."
# patch -uN ./node_modules/parcel-plugin-transcrypt/asset.js <<-END
# --- asset.js	2020-11-30 17:49:49.690000000 -0800
# +++ asset.js	2020-11-30 17:50:42.795302864 -0800
# @@ -1,5 +1,5 @@
#  const Asset = require('parcel-bundler/src/Asset');
# -const logger = require('parcel-bundler/src/Logger');
# +const logger = require('@parcel/logger/src/Logger');
#  const child_process = require('child_process');
#  const path = require('path');
#  const fs = require('fs');
# END
# echo "Transcrypt Parcel Plugin patch completed!"
# echo

#!/bin/bash

echo '#!/bin/bash' > mi_script.sh
echo 'echo "Este es un script creado para DRY7122 S.A."' >> mi_script.sh

chmod +x mi_script.sh

sudo chown root:root mi_script.sh

ls -l mi_script.sh



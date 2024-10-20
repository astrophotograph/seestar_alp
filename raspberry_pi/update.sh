#!/bin/bash -e
src_home=$(cd $(dirname $0)/.. && pwd)
source ${src_home}/raspberry_pi/setup.sh

function update() {
  validate_access

  if [ "$1" = "--force" ]; then
      FORCE=true
  fi

  # check if update is required
  cd "${src_home}"
  git fetch origin
  if [ $(git rev-parse HEAD) = $(git rev-parse @{u}) ] && [ "${FORCE}" != "true" ]; then
      echo "Nothing to do, you're already up-to-date!"
      exit 0
  fi

  if $(systemctl is-active --quiet seestar); then
    sudo systemctl stop seestar
  fi

  if $(systemctl is-active --quiet INDI); then
    sudo systemctl stop INDI
  fi

  cd ${src_home}

  # Perform any update operations here, that need to change
  # prior behavior on the system
  user=$(whoami)
  group=$(id -gn)
  if [ -d ./logs ]; then
      sudo chown ${user}:${group} ./logs/* || true
  else
      mkdir logs
  fi

  config_toml_setup
  install_apt_packages
  python_virtualenv_setup
  systemd_service_setup
  print_banner "update"
}

#
# run update if not sourced from another file
#
(return 0 2>/dev/null) && sourced=1 || sourced=0
if [ ${sourced} = 0 ]; then
    update $@
fi

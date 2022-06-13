#!/usr/bin/env bash
arg=$1
if [ "$arg" = "" ]; then
  echo
  echo "USAGE   : $0 PACKAGES.LIST" 
  echo "EXAMPLE : $0 packages.list.ubt"
  echo
  exit 1
fi

case $(lsb_release -is) in
    Debian)
	sudo ${0%/*}/pkg_install_debian.sh
        ;;
    Ubuntu)
	sudo ${0%/*}/pkg_install_ubuntu.sh
        ;;
    *)
        echo 1>&2 "error: unknown distribution: $(lsb_release -is)"
        exit 1
        ;;
esac

pkgnames=`apt-cache pkgnames`
for package in `sed -e '/^#/D' $arg | xargs`
do
  if echo "$pkgnames" | grep "^$package$" >/dev/null; then
    if [ -n "$ok_pkgs" ]; then
      ok_pkgs="$ok_pkgs $package"
    else
      ok_pkgs=$package
    fi
  else
    if [ -n "$ng_pkgs" ]; then
      ng_pkgs="$ng_pkgs $package"
    else
      ng_pkgs=$package
    fi
  fi
done

sudo apt-get -y --force-yes install $ok_pkgs
if [ $? -eq 0 ]; then
  sudo update-java-alternatives -s java-6-openjdk

  if [ -n "$ng_pkgs" ]; then
    echo "Package installation is incomplete."
    echo "Please download and install these packages:"
    echo $ng_pkgs
    echo
    exit 1
  fi
fi

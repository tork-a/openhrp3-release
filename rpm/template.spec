Name:           ros-indigo-openhrp3
Version:        3.1.7
Release:        14%{?dist}
Summary:        ROS openhrp3 package

Group:          Development/Libraries
License:        EPL
URL:            https://openrtp.jp/svn/hrg/openhrp/
Source0:        %{name}-%{version}.tar.gz

Requires:       atlas-devel
Requires:       boost-devel
Requires:       collada-dom-devel
Requires:       eigen3-devel
Requires:       f2c
Requires:       f2c-libs
Requires:       jython
Requires:       libjpeg-turbo-devel
Requires:       libpng-devel
Requires:       omniORB-devel
Requires:       python-omniORB
Requires:       ros-indigo-openrtm-aist
BuildRequires:  atlas-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  collada-dom-devel
BuildRequires:  doxygen
BuildRequires:  eigen3-devel
BuildRequires:  f2c
BuildRequires:  f2c-libs
BuildRequires:  jython
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  omniORB-devel
BuildRequires:  pkgconfig
BuildRequires:  python-omniORB
BuildRequires:  ros-indigo-openrtm-aist

%description
This package does not only wrap OpenHRP3 but actually provides the built
artifact from the code from its mainstream repository. Being ROS-agnostic by
itself, you can also use this via ROS together with the packages in
rtmros_common that bridge between two framework. OpenHRP3 (Open Architecture
Human-centered Robotics Platform version 3) is an integrated software platform
for robot simulations and software developments. It allows the users to inspect
an original robot model and control program by dynamics simulation. In addition,
OpenHRP3 provides various software components and calculation libraries that can
be used for robotics related software developments (excerpts from here). The
package version number is synchronized to that of mainstream, based on this
decision.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Feb 12 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.1.7-14
- Autogenerated by Bloom

* Wed Feb 11 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.1.7-13
- Autogenerated by Bloom

* Wed Dec 17 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.1.7-12
- Autogenerated by Bloom

* Sun Nov 02 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.1.7-11
- Autogenerated by Bloom

* Sat Nov 01 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.1.7-10
- Autogenerated by Bloom

* Tue Oct 21 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.1.7-9
- Autogenerated by Bloom

* Sun Oct 19 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.1.7-8
- Autogenerated by Bloom

* Mon Oct 06 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.1.7-2
- Autogenerated by Bloom

* Sat Oct 04 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.1.7-0
- Autogenerated by Bloom


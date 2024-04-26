%global forgeurl https://gitlab.com/accounts-sso/signond
%global commit 5b34c5bbc45eedf55bf553675595b3fcb5c156a8
%global date 20220309
Version:        8.61
%global tag VERSION_%{version}
%forgemeta

Name:           signon
Release:        %autorelease
Summary:        Accounts framework for Linux and POSIX based platforms

License:        LGPLv2
URL:            %forgeurl
Source0:        %forgesource

# cmake config files still define SIGNONQT_LIBRARIES_STATIC, but meh, anyone who
# tries to use that deserves what they get
Patch1: signon-8.57-no_static.patch
# drop -Werror -fno-rtti
Patch2: signond-cxxflags.patch

BuildRequires:  make
BuildRequires:  dbus-x11
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libproxy-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  time

# signon-qt5 was in ktp-5 COPR
Obsoletes:      signon-qt5 < 8.57-5
Provides:       signon-qt5 = %{version}-%{release}

# upstream name: signond
Provides:       signond = %{version}-%{release}

# conflicting implementation: gsignond
Conflicts:      gsignond

Requires:       dbus

%description
Single Sign-On is a framework for centrally storing authentication credentials
and handling authentication on behalf of applications as requested by
applications. It consists of a secure storage of login credentials (for example
usernames and passwords), plugins for different authentication systems and a
client library for applications to communicate with this system.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# upstream name: signond
Provides:       signond-devel = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
The %{name}-doc package contains documentation for %{name}.


%prep
%forgesetup

%patch1 -p1 -b .no_static
%patch2 -p1 -b .cxxflags


%build
# Make sure it compiles against Fedora's Qt5
sed -i "s/qdbusxml2cpp/qdbusxml2cpp-qt5/" src/signond/signond.pro

export PATH=%{_qt5_bindir}:$PATH

# FIXME: out-of-src tree build fails -- rex
%qmake_qt5 signon.pro \
  CONFIG+=release \
  QMF_INSTALL_ROOT=%{_prefix} LIBDIR=%{_libdir}

%make_build


%install
make install INSTALL_ROOT=%{buildroot}

# create/own libdir/extensions
mkdir -p %{buildroot}%{_libdir}/extensions/


%check
time \
make check ||:


%ldconfig_scriptlets

%files
## fixme: common/shared _docdir/signon content below gets in the way
#doc README.md TODO NOTES
%license COPYING
%config(noreplace) %{_sysconfdir}/signond.conf
%{_bindir}/signond
%{_bindir}/signonpluginprocess
%{_libdir}/libsignon-extension.so.1*
%{_libdir}/libsignon-plugins-common.so.1*
%{_libdir}/libsignon-plugins.so.1*
%{_libdir}/libsignon-qt5.so.1*
%{_libdir}/signon/
%{_datadir}/dbus-1/services/*.service

%files devel
%{_includedir}/signon-extension/
%{_includedir}/signon-plugins/
%{_includedir}/signon-qt5/
%{_includedir}/signond/
%{_libdir}/cmake/SignOnQt5/
%{_libdir}/libsignon-extension.so
%{_libdir}/libsignon-plugins-common.so
%{_libdir}/libsignon-plugins.so
%{_libdir}/libsignon-qt5.so
%{_libdir}/pkgconfig/SignOnExtension.pc
%{_libdir}/pkgconfig/libsignon-qt5.pc
%{_libdir}/pkgconfig/signon-plugins-common.pc
%{_libdir}/pkgconfig/signon-plugins.pc
%{_libdir}/pkgconfig/signond.pc

%files doc
%{_docdir}/signon/
%{_docdir}/libsignon-qt/
%{_docdir}/signon-plugins/
%{_docdir}/signon-plugins-dev/


%changelog
%autochangelog

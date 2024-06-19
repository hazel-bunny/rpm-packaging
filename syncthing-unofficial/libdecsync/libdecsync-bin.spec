%global _basename libdecsync
%global _libPath %{_basename}/libs
%global debug_package %{nil}

Name:           %{_basename}-bin
Version:        2.2.1

%global forgeurl https://github.com/39aldo39/%{_basename}-bindings-python3
%global tag v%{version}
%global date 20211224
%forgemeta

Release:        2%{?dist}
Summary:        Library for DecSync (Prebuilt)
License:        LGPL-2.0
URL:            %{forgeurl}
Source:         %{forgesource}

Provides:       %{_basename} = %{version}
Conflicts:      %{_basename} = %{version}

ExclusiveArch:  x86_64 aarch64

%ifarch x86_64
%define _suffix amd64
%else
%ifarch aarch64
%define _suffix arm64
%endif
%endif

%description
libdecsync is a multiplatform library for synchronizing using DecSync

This package repackages a prebuilt binary from upstream

%files
%{_libdir}/%{_basename}.so

#-----------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
#nothing

%install
mkdir -p %{buildroot}%{_libdir}
mv %{_libPath}/%{_basename}_%{_suffix}.so %{buildroot}%{_libdir}/%{_basename}.so

%changelog
%autochangelog

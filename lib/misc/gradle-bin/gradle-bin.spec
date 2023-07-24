%global _basename gradle
%global debug_package %{nil}

Name:           %{_basename}-bin
Version:        7.6.2
Release:        %autorelease
Summary:        Gradle Build System

Group:          Development
License:        Apache License 2.0
URL:            https://%{_basename}.org/
Source0:        https://services.%{_basename}.org/distributions/%{_basename}-%{version}-bin.zip

BuildArch:      noarch
BuildRequires:  unzip
Requires:       java

%description
Gradle is a build tool with a focus on build automation and support for multi-
language development. If you are building, testing, publishing, and deploying
software on any platform, Gradle offers a flexible model that can  support the
entire development lifecycle from compiling and packaging code to publishing web
sites. Gradle has been designed to support build automation across multiple
languages and platforms including Java, Scala, Android, C/C++, and Groovy, and
is closely integrated with development tools and continuous integration servers
including Eclipse, IntelliJ, and Jenkins.

%prep
%autosetup -p1

%build
#nothing

%install
mkdir -p %{buildroot}/opt/%{_basename}
cp -R * %{buildroot}/opt/%{_basename}
chmod +x %{buildroot}/opt/%{_basename}/bin/%{_basename}

mkdir -p %{buildroot}/usr/bin
ln -s /opt/%{_basename}/bin/%{_basename} %{buildroot}/usr/bin

rm %{buildroot}/opt/%{_basename}/bin/%{_basename}.bat
rm -rf %{buildroot}/opt/%{_basename}/init.d

%files
/opt/%{_basename}
%{_bindir}/%{_basename}

%changelog
* Mon Jul 24 2023 Dipta Biswas <dab@gmail.com> 6.3-1
- Initial version.

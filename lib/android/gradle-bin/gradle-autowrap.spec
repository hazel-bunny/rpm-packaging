%global forgeurl https://github.com/emlun/gradle-autowrap
%global tag v1.1.1
%forgemeta

Name:    gradle-autowrap
Version: 1.1.1
Release: %autorelease
License: Unlicense
Summary: Gradle Wrapper
URL:     %{forgeurl}
Source:  %{forgesource}

BuildArch: noarch
Requires:  gradle

%description
Entry script for Gradle that walks up the directory tree and calls the closest Gradle wrapper if it exists, falling back on /usr/bin/gradle if no wrapper is found.

The script assumes that all your Gradle wrappers have the file name gradlew and that your system Gradle binary is /usr/bin/gradle.

%prep
%forgeautosetup

%build
#nothing

%install
install -Dm 555 gradle-autowrap.sh %{buildroot}%{prefix}/local/bin/gradle
install -Dm 444 UNLICENSE %{buildroot}%{datadir}/licenses/%{name}/UNLICENSE

%check
#nothing

%files
%license UNLICENSE
%doc README.md
%{prefix}/local/bin/gradle

%changelog
%autochangelog

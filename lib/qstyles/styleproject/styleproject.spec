%global forgeurl https://sourceforge.net/p/styleproject
%global commit
%global date 2022
%forgemeta

Name:    styleproject
Version:
Release: %autorelease
Summary:
URL:     %{forgeurl}
Source:  %{forgesource}

%description

%files
%license
%doc

%prep
%forgeautosetup

%changelog
%autochangelog

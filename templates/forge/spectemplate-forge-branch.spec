# This template shows how to package a branch state using the forgemeta macro.
#
# BRANCH STATES ARE NOT REPRODUCIBLE AND SHOULD NEVER BE SHARED WITH OTHERS.
#
# For more explanations on forgemeta, read the forgemeta-release template.
#
# The project url on the forge
%global forgeurl
#
# The branch being packaged
%global branch
#
#  – use the “-i” flag to display the variables forgemeta reads and sets
#  – use the “-v” flag if you want verbose processing
#  – remove  “-i” and “-v” before commit
%forgemeta

# The following lines use variables computed by forgemeta as default values.
# You can replace them with manual definitions.
# forgemeta will prepend branch information to dist. Release ordering is
# controlled by the packager with x%{?dist}/0.x%{?dist} number chains.
Name:
Version:
Release: 1%{?dist}
Summary:
URL:	 %{forgeurl}
Source:  %{forgesource}
%description


%prep
#  – an autosetup wrapper, forgeautosetup, is also provided
#  – use the “-v” flag if you want verbose processing; remove it before commit
#  – call forgesetup/autosetup directly if you do not like the result
%forgesetup
#
# After this point the archive extraction is done. forgemeta is no longer used.

%build

%install

%check

%files
%license
%doc

%changelog

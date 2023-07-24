# This template shows how to package a tag state using the forgemeta macro.
# For more explanations on forgemeta, read the forgemeta-release template.
#
# The project url on the forge
%global forgeurl
#
# The tag being packaged
%global tag
#
#  – use the “-i” flag to display the variables forgemeta reads and sets
#  – use the “-v” flag if you want verbose processing
#  – remove  “-i” and “-v” before commit
%forgemeta

# The following lines use variables computed by forgemeta as default values.
# You can replace them with manual definitions.
# forgemeta will prepend tag information to dist. Release ordering is
# controlled by the packager with x%{?dist}/0.x%{?dist} numbers chains.
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

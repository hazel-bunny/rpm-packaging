# This template shows how to package a commit state using the forgemeta macro.
# That should be the default target use case.
# Other less common use cases are documented in separate templates.
#
# The project url on the forge, for example
# https://gitlab.gnome.org/GNOME/gtk/
%global forgeurl
#
# Packaging a release requires setting Version before calling forgemeta.
# Because most forges follow the git model, and git made no provision for
# release objects, forgemeta will try to guess the customary way to write
# release tags on the selected forge.
# If it guesses wrong use the forge-tag template instead of this one.
Version:
#
# forgemeta converts the suppplied rpm variables to variables that can be used
# in the spec file. Most of those can be overriden before or after the
# forgemeta call.
#  – use the “-i” flag to display the variables forgemeta reads and sets
#  – use the “-v” flag if you want verbose processing
#  – remove  “-i” and “-v” before commit
%forgemeta

# The following lines use  variables computed by forgemeta as default values.
# You can replace them with manual definitions. For example, replace forgeurl
# with the project homepage if it exists separately from the repository URL.
# Only replace the variables when it adds value to the spec file and you
# understand the consequences. Release ordering is controlled by the packager
# with x%{?dist}/0.x%{?dist} number chains.
Name:
Release: 1%{?dist}
Summary:
URL:	 %{forgeurl}
Source:  %{forgesource}
%description


%prep
# forgesetup calls setup with the correct flags for archives downloaded from
# the selected forge. A forgeautosetup autosetup wrapper is also provided. If
# you disagree with the computed setup/autosetup flags, just call
# setup/autosetup directly.
#  – use the “-v” flag if you want verbose processing
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

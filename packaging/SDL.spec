Name:       SDL
Summary:    An SDL app
Version:    0.0.1
Release:    1
Group:      Applications/System
License:    ASL 2.0
URL:        http://www.tizen.org
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  common
BuildRequires:  zip
BuildRequires:  desktop-file-utils
Requires:   wrt-installer
Requires:   wrt-plugins-ivi

%description
An application for SDL.

%prep
%setup -q -n %{name}-%{version}

%build
make wgtPkg

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/opt/usr/apps/.preinstallWidgets/SDL.wgt

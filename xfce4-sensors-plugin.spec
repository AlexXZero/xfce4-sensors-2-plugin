Summary: 	Sensors plugin for the Xfce panel
Name: 		xfce4-sensors-plugin
Version: 	0.10.99.8
Release: 	1
License:	GPL
URL: 		http://goodies.xfce.org/projects/panel-plugins/xfce4-sensors-plugin
Source0: 	%{name}-%{version}.tar.gz
Group: 		User Interface/Desktops
BuildRoot: 	%{_tmppath}/%{name}-root
Requires:	xfce4-panel >= @XFCE4_PANEL_REQUIRED_VERSION@
BuildRequires:	xfce4-panel >= @XFCE4_PANEL_REQUIRED_VERSION@
Requires:	lm_sensors >= 2.8
BuildRequires:	lm_sensors-devel >= 2.8

%description
This plugin displays various hardware sensor values in the Xfce panel.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README TODO
%{_libdir}/xfce4/panel-plugins/
%{_datadir}/

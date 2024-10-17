%define name gai-visual-audio
%define version 0.3
%define release %mkrel 12

Name: %name
Summary: GAI applet Visualizing the XMMS output
Version: %{version}
Release: %{release}
License: GPL
Url: https://gai.sf.net
Group: Sound
Source: http://prdownloads.sourceforge.net/gai/%{name}-%{version}.tar.bz2
Source10:   %{name}-16.png
Source11:   %{name}-32.png
Source12:   %{name}-48.png
BuildRoot: %{_tmppath}/build-root-%{name}
BuildRequires: libgai-devel >= 0.5
BuildRequires: xmms-devel

%description
GAI applet Visualizing the XMMS output. This can be used in several
panels, inlcuding the GNOME one.

%prep
%setup -q 

%build
%configure2_5x
%make 

%install
rm -rf ${RPM_BUILD_ROOT}
install -m755 gai-va -D $RPM_BUILD_ROOT%{_bindir}/gai-va
install -m644 GNOME_DefaultApplet.server -D $RPM_BUILD_ROOT%{_libdir}/bonobo/servers/GNOME_gai-vaApplet.server
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps/gai-va/
install -m644 images/* $RPM_BUILD_ROOT%{_datadir}/pixmaps/gai-va/
install -m644 gai-va-icon.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/
install -m644 %SOURCE10 -D %{buildroot}/%_miconsdir/%name.png
install -m644 %SOURCE11 -D %{buildroot}/%_iconsdir/%name.png
install -m644 %SOURCE12 -D %{buildroot}/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Gai-visual-studio
Comment=Visualizing the XMMS output
Exec=%{_bindir}/%{name}
Icon=%name
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio;
StartupNotify=true
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root,0755)
%doc AUTHORS INSTALL README
%{_bindir}/*
%{_libdir}/bonobo/servers/GNOME_gai-vaApplet.server
%_datadir/applications/mandriva*
%{_datadir}/pixmaps/gai-va/
%{_datadir}/pixmaps/gai-va-icon.png
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png
%{_miconsdir}/%name.png



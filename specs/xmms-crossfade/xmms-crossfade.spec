# $Id$
# Authority: matthias
# Upstream: Peter Eisenlohr <p.eisenlohr@gmx.net>

%define xmms_outputdir %(xmms-config --output-plugin-dir)

Summary: Crossfade output plugin for XMMS
Name: xmms-crossfade
Version: 0.3.4
Release: 2
License: GPL
Group: Applications/Multimedia
URL: http://www.netcologne.de/~nc-eisenlpe2/xmms-crossfade/
Source: http://www.netcologne.de/~nc-eisenlpe2/xmms-crossfade/xmms-crossfade-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xmms >= 1.0.0, glib >= 1.2.7, gtk+ >= 1.2.7
BuildRequires: xmms-devel, gtk+-devel


%description
A neat crossfade plugin for XMMS featuring crossfading and continuous output
between songs and a gap-killer.


%prep
%setup


%build
%configure --libdir="%{xmms_outputdir}"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall libdir="%{buildroot}/%{xmms_outputdir}"


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%{xmms_outputdir}/libcrossfade.so
%exclude %{xmms_outputdir}/libcrossfade.la


%changelog
* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.3.4-3
- Rebuild for Fedora Core 2.
- Removed explicit stripping, that's for the debuginfo package now.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.3.4-2
- Rebuild for Fedora Core 1.

* Wed Oct  8 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.4.

* Mon Oct  6 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.3.

* Tue Apr 22 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.2.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Thu Mar 13 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.1.

* Sat Sep 28 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Changed the hard-coded Output dir to a value expanded from xmms-config.
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Mon Jun 11 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.9.

* Sat May 12 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.8.

* Mon Apr 23 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.7.

* Fri Apr 20 2001 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat 7.1.

* Sun Mar 25 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.6.

* Thu Mar 15 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.5.

* Mon Mar 12 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.4.

* Tue Jan  2 2001 Matthias Saou <http://freshrpms.net/>
- Initial RedHat 7.0 RPM release


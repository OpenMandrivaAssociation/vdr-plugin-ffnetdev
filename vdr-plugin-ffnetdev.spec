
%define plugin	ffnetdev
%define name	vdr-plugin-%plugin
%define version	0.1.0
%define snapshot 33
%define rel	5

Summary:	VDR plugin: Full Featured Network Device for Streaming
Name:		%name
Version:	%version
%if %snapshot
Release:	%mkrel 12.svn%snapshot.%rel
%else
Release:	%mkrel %rel
%endif
Group:		Video
License:	GPL+
URL:		http://developer.berlios.de/projects/ffnetdev
%if %snapshot
Source:		vdr-%plugin-%snapshot.tar.bz2
%else
Source:		http://download.berlios.de/ffnetdev/vdr-%plugin-%version.tar.bz2
%endif
Patch0:		ffnetdev-i18n-1.6.patch
Patch1:		91_ffnetdev-0.1.0+svn20060625-1.5.0.dpatch
Patch2:		92_vdr-1.5.12-ffnetdev-svn20071122.dpatch
Patch3:		ffnetdev-duplicate-param-name.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
The purpose of this plugin is to provide an "easy" way of connecting
possible streaming clients to VDR by emulating a full featured DVB
device over the network including OSD and TS streaming capabilities.

%prep
%if %snapshot
%setup -q -n %plugin-%snapshot
%else
%setup -q -n vdr-%plugin-%version
%endif
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# port number for sending TS to
var=TS_PORT
param="-t TS_PORT"
# listen on this port for OSD connect
var=OSD_PORT
param="-o OSD_PORT"
# listen on this port for ClientControl connection
var=CONTROL_PORT
param="-c CONTROL_PORT"
# enable remote control over OSD connection
var=OSD_CONTROL
param=-e
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README CHANGELOG




%changelog
* Thu Jul 30 2009 Anssi Hannula <anssi@mandriva.org> 0.1.0-12.svn33.5mdv2011.0
+ Revision: 404570
- rebuild due to BS building the previous release against wrong VDR on i586

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1.0-12.svn33.4mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 0.1.0-12.svn33.3mdv2009.1
+ Revision: 359706
- fix typo in function declaration (duplicate-param-name.patch)
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.1.0-12.svn33.2mdv2009.0
+ Revision: 197931
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.1.0-12.svn33.1mdv2009.0
+ Revision: 197674
- new snapshot
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- adapt for api changes of vdr 1.5.0 (P1 from e-tobi)
- adapt for api changes of vdr 1.5.12 (P2 from e-tobi)
- add new option to sysconfig
- apply new license policy

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.1.0-12mdv2008.1
+ Revision: 145097
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.1.0-11mdv2008.1
+ Revision: 103096
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.1.0-10mdv2008.0
+ Revision: 50002
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 9mdv2008.0-current
+ Revision: 42088
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.1.0-8mdv2008.0
+ Revision: 22675
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-7mdv2007.0
+ Revision: 90925
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-6mdv2007.1
+ Revision: 74016
- rebuild for new vdr
- Import vdr-plugin-ffnetdev

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-2mdv2007.0
- rebuild for new vdr

* Thu Jul 13 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-1mdv2007.0
- initial Mandriva release


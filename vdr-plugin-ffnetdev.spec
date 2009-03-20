
%define plugin	ffnetdev
%define name	vdr-plugin-%plugin
%define version	0.1.0
%define snapshot 33
%define rel	3

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



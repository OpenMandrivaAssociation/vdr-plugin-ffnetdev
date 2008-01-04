
%define plugin	ffnetdev
%define name	vdr-plugin-%plugin
%define version	0.1.0
%define rel	12

Summary:	VDR plugin: Full Featured Network Device for Streaming
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://developer.berlios.de/projects/ffnetdev
Source:		http://download.berlios.de/ffnetdev/vdr-%plugin-%version.tar.bz2
Patch1:		vdr-ffnetdev-active.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
The purpose of this plugin is to provide an "easy" way of connecting
possible streaming clients to VDR by emulating a full featured DVB
device over the network including OSD and TS streaming capabilities.

%prep
%setup -q -n vdr-%plugin-%version
%patch1 -p1 -b .active

%vdr_plugin_params_begin %plugin
# port number for sending TS to
var=TS_PORT
param="-t TS_PORT"
# listen on this port for OSD connect
var=OSD_PORT
param="-o OSD_PORT"
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



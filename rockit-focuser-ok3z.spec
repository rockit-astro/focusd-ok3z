Name:      rockit-focuser-ok3z
Version:   %{_version}
Release:   1
Summary:   ASA ok3zfocuser.
Url:       https://github.com/rockit-astro/focusd-ok3z
License:   GPL-3.0
BuildArch: noarch

%description


%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/etc/bash_completion.d
mkdir -p %{buildroot}%{_sysconfdir}/focusd/
mkdir -p %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/focus %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/focusd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/focusd@.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/completion/focus %{buildroot}/etc/bash_completion.d

%{__install} %{_sourcedir}/ngts_m06.json %{buildroot}%{_sysconfdir}/focusd/

%package server
Summary:  Focuser control server.
Group:    Unspecified
Requires: python3-rockit-focuser-ok3z python3-pyserial
%description server

%files server
%defattr(0755,root,root,-)
%{_bindir}/focusd
%defattr(0644,root,root,-)
%{_unitdir}/focusd@.service

%package client
Summary:  Focuser control client.
Group:    Unspecified
Requires: python3-rockit-focuser-ok3z
%description client

%files client
%defattr(0755,root,root,-)
%{_bindir}/focus
/etc/bash_completion.d/focus

%package data-ngts-m06
Summary: Focuser data for NGTS M06
Group:   Unspecified
%description data-ngts-m06

%files data-ngts-m06
%defattr(0644,root,root,-)
%{_sysconfdir}/focusd/ngts_m06.json

%changelog

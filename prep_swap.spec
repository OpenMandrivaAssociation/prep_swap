%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	Tool to prepare swap for LTSP
Name:		prep_swap
Version:	0.02
Release:	%mkrel 5
License:	GPL
Group:		System/Servers
URL:		http://www.ltsp.org
Source0:	http://www.ltsp.org/tarballs/%{name}-%{version}.tar.bz2
BuildRequires:	uClibc-popt-devel
BuildRequires:	uClibc-devel
BuildRequires:	uClibc-static-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This daemon will run on a workstation, listening on a port (9200) for a command
to run.  Initially, the first command will be a 'get' command, for retrieving
configuration things, like the sound daemon entry.

%prep

%setup -q -n %{name}-%{version}

%build
uclibc gcc -Os -Wl,-Bstatic -L%{_prefix}/%{_target_cpu}-linux-uclibc/usr/lib \
    -o %{name} %{name}.c %{_prefix}/%{_target_cpu}-linux-uclibc/usr/lib/libpopt.a

%install
rm -rf %{buildroot}

install -d %{buildroot}/sbin
install -m0755 %{name} %{buildroot}/sbin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%attr(0755,root,root) /sbin/%{name}



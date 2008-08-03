Summary:	Displays the uptime in a human readable format
Name:		up
Version:	0.3
Release:	%mkrel 11
License:	GPL
Group:		System/Base
URL:		http://www.burdell.org/up.php3
Source:		%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
up displays the uptime of the system accounting for decades, years, weeks,
days, hours, and minutes.  It can output the uptime in its standard hardcore
format or the standard 'uptime' (that program that comes with procps) format
for quick comparisons with other systems.

%prep

%setup -n %{name}-%{version}

%build
gcc %{optflags} -o up up.c

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m755 up %{buildroot}%{_bindir}/
install -m644 up.1 %{buildroot}%{_mandir}/man1/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_bindir}/*
%{_mandir}/man1/*

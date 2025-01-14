# Based on Fedora's package

%define tar_release a9

Name:    lmbench
Version: 3.0
Release: %mkrel 0.%{tar_release}.3
Summary: Tools for Kernel Performance Analysis
License: GPL
URL:	 https://sourceforge.net/projects/lmbench
Source: http://dl.sf.net/lmbench/lmbench-%{version}-%{tar_release}.tgz
Source1: %{name}-%{version}-%{tar_release}-run.sh
Group: Development/Kernel
Requires: perl, make
BuildRoot: %{_tmppath}/%{name}-%{version}-%{tar_release}-root

%description
Bandwidth benchmarks: cached file read, memory copy (bcopy), memory read,
memory write, pipe, TCP; Latency benchmarks: context switching, connection
establishment, pipe, TCP, UDP, RPC hot potato, file system creates and
deletes, process creation, signal handling, system call overhead,  memory
read latency; Miscellanious Processor clock rate calculation.

%prep
%setup -q -n %{name}-%{version}-%{tar_release}

mv -f src/TODO TODO.lmbench
mv -f scripts/README README.scripts
mv -f scripts/SHIT SHIT.scripts
mv -f scripts/TODO TODO.scripts

%build
%{make}
find . -name 'SCCS' -type d -exec rm -rf {} \;

%install
rm -rf %{buildroot}

install -Dp -m0755 %{SOURCE1} %{buildroot}%{_bindir}/lmbench
install -Dp -m0644 results/Makefile %{buildroot}%{_prefix}/lib/lmbench/results/Makefile
install -Dp -m0644 src/webpage-lm.tar %{buildroot}%{_prefix}/lib/lmbench/src/webpage-lm.tar

cp -avx bin/ scripts/ %{buildroot}%{_prefix}/lib/lmbench/
find %{buildroot}%{_prefix}/lib/lmbench/ -name 'Makefile*' -or -name '*.[ao]' -exec %{__rm} -f {} \;

chmod a-x %{buildroot}%{_prefix}/lib/lmbench/scripts/info-template

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ACKNOWLEDGEMENTS CHANGES COPYING COPYING-2 hbench-REBUTTAL README.* TODO.* doc/
%{_bindir}/lmbench
%{_prefix}/lib/lmbench/


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0-0.a9.3mdv2011.0
+ Revision: 620248
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 3.0-0.a9.2mdv2010.0
+ Revision: 439561
- rebuild

* Thu Jan 15 2009 Luiz Fernando Capitulino <lcapitulino@mandriva.com> 3.0-0.a9.1mdv2009.1
+ Revision: 329890
- import lmbench



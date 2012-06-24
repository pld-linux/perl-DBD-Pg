%define		_noautoreq "perl(POSIX(qw(isprint)))"
%include	/usr/lib/rpm/macros.perl
Summary:	DBD-Pg perl module
Summary(pl):	Modu� perla DBD-Pg
Name:		perl-DBD-Pg
Version:	1.01
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBD/DBD-Pg-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-DBI
BuildRequires:	postgresql-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::Pg - PostgreSQL database driver for the DBI module.

%description -l pl
DBD::Pg - Sterownik bazy danych PostgreSQL dla modu�u DBI.

%prep
%setup -q -n DBD-Pg-%{version}

%build
POSTGRES_LIB="%{_libdir}"; export POSTGRES_LIB
POSTGRES_INCLUDE="%{_includedir}/postgresql"; export POSTGRES_INCLUDE
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/DBD/*.pm
%{perl_sitearch}/auto/DBD/Pg/Pg.bs
%attr(755,root,root) %{perl_sitearch}/auto/DBD/Pg/Pg.so
%{_mandir}/man[13]/*

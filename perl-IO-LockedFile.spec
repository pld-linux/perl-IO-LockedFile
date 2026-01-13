#
# Conditional build:
%bcond_with	tests		# perform "make test"
#
%define	pdir	IO
%define	pnam	LockedFile
Summary:	IO::LockedFile - supply object methods for locking files
Summary(pl.UTF-8):	IO::LockedFile - metody obiektów do blokowania blików
Name:		perl-IO-LockedFile
Version:	0.23
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f447f67ac7c9f42d86d07ca7477cdec6
URL:		http://search.cpan.org/dist/IO-LockedFile/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In its simplistic use, the IO::LockedFile class gives us the same
interface of the IO::File class with the unique difference that the
files we deal with are locked using the Flock mechanism (using the
flock function).

%description -l pl.UTF-8
W najprostszym zastosowaniu klasa IO::LockedFile udostępnia ten sam
interfejs, co klasa IO::File z jedyną różnicą polegającą na tym, że
pliki są blokowane przy użyciu mechanizmu Flock (przy użyciu funkcji
flock).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IO/*.pm
%{perl_vendorlib}/IO/LockedFile
%{_mandir}/man3/*

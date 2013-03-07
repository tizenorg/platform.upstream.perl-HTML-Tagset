Name:           perl-HTML-Tagset
Version:        3.20
Release:        0
License:        GPL-2.0+ or Artistic
Summary:        HTML::Tagset - data tables useful in parsing HTML
Url:            http://search.cpan.org/dist/HTML-Tagset/
Group:          Development/Libraries
Source0:        HTML-Tagset-%{version}.tar.gz
BuildRequires:  perl
BuildArch:      noarch

%description
This module contains several data tables useful in various kinds of
HTML parsing operations, such as tag and entity names.

%prep
%setup -q -n HTML-Tagset-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files

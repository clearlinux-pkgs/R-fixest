#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fixest
Version  : 0.10.4
Release  : 6
URL      : https://cran.r-project.org/src/contrib/fixest_0.10.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fixest_0.10.4.tar.gz
Summary  : Fast Fixed-Effects Estimations
Group    : Development/Tools
License  : GPL-3.0
Requires: R-fixest-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-dreamerr
Requires: R-numDeriv
Requires: R-sandwich
BuildRequires : R-Rcpp
BuildRequires : R-data.table
BuildRequires : R-dreamerr
BuildRequires : R-numDeriv
BuildRequires : R-sandwich
BuildRequires : buildreq-R

%description
# fixest: Fast and user-friendly fixed-effects estimation
<a href="https://cran.r-project.org/web/checks/check_results_fixest.html"><img src="https://cranchecks.info/badges/worst/fixest" alt="CRAN status"></a>
<a href="https://CRAN.R-project.org/package=fixest"><img src="http://www.r-pkg.org/badges/version/fixest" alt="Version"> </a>
<a href="https://ipub.com/dev-corner/apps/r-package-downloads/"> <img src="https://cranlogs.r-pkg.org/badges/fixest" alt = "Downloads"> </a>

%package lib
Summary: lib components for the R-fixest package.
Group: Libraries

%description lib
lib components for the R-fixest package.


%prep
%setup -q -c -n fixest
cd %{_builddir}/fixest

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1648827097

%install
export SOURCE_DATE_EPOCH=1648827097
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fixest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fixest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fixest
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fixest || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fixest/CITATION
/usr/lib64/R/library/fixest/DESCRIPTION
/usr/lib64/R/library/fixest/INDEX
/usr/lib64/R/library/fixest/Meta/Rd.rds
/usr/lib64/R/library/fixest/Meta/data.rds
/usr/lib64/R/library/fixest/Meta/demo.rds
/usr/lib64/R/library/fixest/Meta/features.rds
/usr/lib64/R/library/fixest/Meta/hsearch.rds
/usr/lib64/R/library/fixest/Meta/links.rds
/usr/lib64/R/library/fixest/Meta/nsInfo.rds
/usr/lib64/R/library/fixest/Meta/package.rds
/usr/lib64/R/library/fixest/Meta/vignette.rds
/usr/lib64/R/library/fixest/NAMESPACE
/usr/lib64/R/library/fixest/NEWS.md
/usr/lib64/R/library/fixest/R/fixest
/usr/lib64/R/library/fixest/R/fixest.rdb
/usr/lib64/R/library/fixest/R/fixest.rdx
/usr/lib64/R/library/fixest/data/Rdata.rdb
/usr/lib64/R/library/fixest/data/Rdata.rds
/usr/lib64/R/library/fixest/data/Rdata.rdx
/usr/lib64/R/library/fixest/data/datalist
/usr/lib64/R/library/fixest/demo/femlm.R
/usr/lib64/R/library/fixest/doc/exporting_tables.R
/usr/lib64/R/library/fixest/doc/exporting_tables.Rmd
/usr/lib64/R/library/fixest/doc/exporting_tables.html
/usr/lib64/R/library/fixest/doc/fixest_walkthrough.R
/usr/lib64/R/library/fixest/doc/fixest_walkthrough.Rmd
/usr/lib64/R/library/fixest/doc/fixest_walkthrough.html
/usr/lib64/R/library/fixest/doc/index.html
/usr/lib64/R/library/fixest/doc/multiple_estimations.R
/usr/lib64/R/library/fixest/doc/multiple_estimations.Rmd
/usr/lib64/R/library/fixest/doc/multiple_estimations.html
/usr/lib64/R/library/fixest/doc/standard_errors.R
/usr/lib64/R/library/fixest/doc/standard_errors.Rmd
/usr/lib64/R/library/fixest/doc/standard_errors.html
/usr/lib64/R/library/fixest/help/AnIndex
/usr/lib64/R/library/fixest/help/aliases.rds
/usr/lib64/R/library/fixest/help/fixest.rdb
/usr/lib64/R/library/fixest/help/fixest.rdx
/usr/lib64/R/library/fixest/help/paths.rds
/usr/lib64/R/library/fixest/html/00Index.html
/usr/lib64/R/library/fixest/html/R.css
/usr/lib64/R/library/fixest/tests/fixest_tests.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/fixest/libs/fixest.so
/usr/lib64/R/library/fixest/libs/fixest.so.avx2
/usr/lib64/R/library/fixest/libs/fixest.so.avx512

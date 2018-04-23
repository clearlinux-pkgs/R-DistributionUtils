#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-DistributionUtils
Version  : 0.5.1
Release  : 5
URL      : https://cran.r-project.org/src/contrib/DistributionUtils_0.5-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/DistributionUtils_0.5-1.tar.gz
Summary  : Distribution Utilities
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-DistributionUtils-lib
Requires: R-RUnit
BuildRequires : R-RUnit
BuildRequires : clr-R-helpers

%description
packages I have developed for dealing with distributions.
        Currently these packages are GeneralizedHyperbolic,
        VarianceGamma, and SkewHyperbolic and NormalLaplace. Each of
        these packages requires DistributionUtils. Functionality
        includes sample skewness and kurtosis, log-histogram, tail
        plots, moments by integration, changing the point about which a
        moment is calculated, functions for testing distributions using
        inversion tests and the Massart inequality. Also includes an
        implementation of the incomplete Bessel K function.

%package lib
Summary: lib components for the R-DistributionUtils package.
Group: Libraries

%description lib
lib components for the R-DistributionUtils package.


%prep
%setup -q -c -n DistributionUtils

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523302113

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523302113
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DistributionUtils
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DistributionUtils
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DistributionUtils
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library DistributionUtils|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/DistributionUtils/DESCRIPTION
/usr/lib64/R/library/DistributionUtils/INDEX
/usr/lib64/R/library/DistributionUtils/Meta/Rd.rds
/usr/lib64/R/library/DistributionUtils/Meta/features.rds
/usr/lib64/R/library/DistributionUtils/Meta/hsearch.rds
/usr/lib64/R/library/DistributionUtils/Meta/links.rds
/usr/lib64/R/library/DistributionUtils/Meta/nsInfo.rds
/usr/lib64/R/library/DistributionUtils/Meta/package.rds
/usr/lib64/R/library/DistributionUtils/NAMESPACE
/usr/lib64/R/library/DistributionUtils/NEWS
/usr/lib64/R/library/DistributionUtils/R/DistributionUtils
/usr/lib64/R/library/DistributionUtils/R/DistributionUtils.rdb
/usr/lib64/R/library/DistributionUtils/R/DistributionUtils.rdx
/usr/lib64/R/library/DistributionUtils/help/AnIndex
/usr/lib64/R/library/DistributionUtils/help/DistributionUtils.rdb
/usr/lib64/R/library/DistributionUtils/help/DistributionUtils.rdx
/usr/lib64/R/library/DistributionUtils/help/aliases.rds
/usr/lib64/R/library/DistributionUtils/help/paths.rds
/usr/lib64/R/library/DistributionUtils/html/00Index.html
/usr/lib64/R/library/DistributionUtils/html/R.css
/usr/lib64/R/library/DistributionUtils/libs/symbols.rds
/usr/lib64/R/library/DistributionUtils/unitTests/Makefile
/usr/lib64/R/library/DistributionUtils/unitTests/report.html
/usr/lib64/R/library/DistributionUtils/unitTests/report.txt
/usr/lib64/R/library/DistributionUtils/unitTests/reportSummary.txt
/usr/lib64/R/library/DistributionUtils/unitTests/runTests.R
/usr/lib64/R/library/DistributionUtils/unitTests/runit.besselRatio.R
/usr/lib64/R/library/DistributionUtils/unitTests/runit.distIneqMassart.R
/usr/lib64/R/library/DistributionUtils/unitTests/runit.incompleteBesselK.R
/usr/lib64/R/library/DistributionUtils/unitTests/runit.integrateDens.R
/usr/lib64/R/library/DistributionUtils/unitTests/runit.inversionTests.R
/usr/lib64/R/library/DistributionUtils/unitTests/runit.iswholenumber.R
/usr/lib64/R/library/DistributionUtils/unitTests/runit.logHist.R
/usr/lib64/R/library/DistributionUtils/unitTests/runit.momChangeAbout.R
/usr/lib64/R/library/DistributionUtils/unitTests/runit.momIntegrated.R
/usr/lib64/R/library/DistributionUtils/unitTests/runit.momSE.R
/usr/lib64/R/library/DistributionUtils/unitTests/runit.safeIntegrate.R
/usr/lib64/R/library/DistributionUtils/unitTests/runit.sampleMoments.R
/usr/lib64/R/library/DistributionUtils/unitTests/runit.tailPlot.R
/usr/lib64/R/library/DistributionUtils/unitTests/runit.testTestScheme.R
/usr/lib64/R/library/DistributionUtils/unitTests/runit.tsHessian.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/DistributionUtils/libs/DistributionUtils.so
/usr/lib64/R/library/DistributionUtils/libs/DistributionUtils.so.avx2
/usr/lib64/R/library/DistributionUtils/libs/DistributionUtils.so.avx512

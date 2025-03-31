#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v22
# autospec commit: 247c192
#
Name     : R-DistributionUtils
Version  : 0.6.2
Release  : 56
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/DistributionUtils_0.6-2.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/DistributionUtils_0.6-2.tar.gz
Summary  : Distribution Utilities
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-DistributionUtils-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
packages I have developed for dealing with
    distributions. Currently these packages are GeneralizedHyperbolic,
    VarianceGamma, and SkewHyperbolic and NormalLaplace. Each of these
    packages requires DistributionUtils. Functionality includes sample
    skewness and kurtosis, log-histogram, tail plots, moments by
    integration, changing the point about which a moment is
    calculated, functions for testing distributions using inversion
    tests and the Massart inequality. Also includes an implementation
    of the incomplete Bessel K function.

%package lib
Summary: lib components for the R-DistributionUtils package.
Group: Libraries

%description lib
lib components for the R-DistributionUtils package.


%prep
%setup -q -n DistributionUtils
pushd ..
cp -a DistributionUtils buildavx2
popd
pushd ..
cp -a DistributionUtils buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1743432011

%install
export SOURCE_DATE_EPOCH=1743432011
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/DistributionUtils/tests/doRUnit.R
/usr/lib64/R/library/DistributionUtils/unitTests/Makefile
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
/V3/usr/lib64/R/library/DistributionUtils/libs/DistributionUtils.so
/V4/usr/lib64/R/library/DistributionUtils/libs/DistributionUtils.so
/usr/lib64/R/library/DistributionUtils/libs/DistributionUtils.so

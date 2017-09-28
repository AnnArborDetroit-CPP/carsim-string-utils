from conans import ConanFile, CMake, tools


class CarsimstringutilsConan(ConanFile):
    name = "carsim-string-utils"
    version = "0.1.0"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Carsimstringutils here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    exports_sources = "*.sln", "*.cpp", "*.h", "*.vcxproj", "*.filters"

    def build(self):
        #  set "VSCMD_START_DIR=%CD%" && 
        #  call "C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\Tools\../../VC/Auxiliary/Build/vcvarsall.bat" amd64 && 
        #  devenv carsim-string-utils.sln /upgrade && 
        #  msbuild carsim-string-utils.sln /p:Configuration=Release /p:Platform="x64" /target:carsim-string-utils
        
        build_command = tools.msvc_build_command(self.settings, "carsim-string-utils.sln", targets=["carsim-string-utils"])
        self.run(build_command)

    def package(self):
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        tools.collect_libs(self)
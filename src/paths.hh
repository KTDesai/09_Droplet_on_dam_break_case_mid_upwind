#ifndef PATHS_HH
#define PATHS_HH

#include <string>

namespace paths
{
  inline const std::string mesh         = "mesh/";
  inline const std::string results      = "results/";
  inline const std::string fields       = results + "fields/";
  inline const std::string residuals    = results + "residuals/";
  inline const std::string coefficients = results + "coefficients/";
}

#endif

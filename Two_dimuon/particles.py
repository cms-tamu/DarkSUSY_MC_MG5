# This file was automatically created by FeynRules $Revision: 535 $
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (November 6, 2010)
# Date: Wed 23 Mar 2011 22:58:09


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

ve = Particle(pdg_code = 12,
              name = 've',
              antiname = 've~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 've',
              antitexname = 've~',
              charge = 0,
              LeptonNumber = 1,
              GhostNumber = 0)

ve__tilde__ = ve.anti()

vm = Particle(pdg_code = 14,
              name = 'vm',
              antiname = 'vm~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vm',
              antitexname = 'vm~',
              charge = 0,
              LeptonNumber = 1,
              GhostNumber = 0)

vm__tilde__ = vm.anti()

vt = Particle(pdg_code = 16,
              name = 'vt',
              antiname = 'vt~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vt',
              antitexname = 'vt~',
              charge = 0,
              LeptonNumber = 1,
              GhostNumber = 0)

vt__tilde__ = vt.anti()

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.ZERO,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      charge = -1,
                      LeptonNumber = 1,
                      GhostNumber = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                      name = 'mu-',
                      antiname = 'mu+',
                      spin = 2,
                      color = 1,
                      mass = Param.MM,
                      width = Param.ZERO,
                      texname = 'mu-',
                      antitexname = 'mu+',
                      charge = -1,
                      LeptonNumber = 1,
                      GhostNumber = 0)

mu__plus__ = mu__minus__.anti()

ta__minus__ = Particle(pdg_code = 15,
                       name = 'ta-',
                       antiname = 'ta+',
                       spin = 2,
                       color = 1,
                       mass = Param.ZERO,
                       width = Param.ZERO,
                       texname = 'ta-',
                       antitexname = 'ta+',
                       charge = -1,
                       LeptonNumber = 1,
                       GhostNumber = 0)

ta__plus__ = ta__minus__.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u~',
             charge = 2/3,
             LeptonNumber = 0,
             GhostNumber = 0)

u__tilde__ = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'c~',
             charge = 2/3,
             LeptonNumber = 0,
             GhostNumber = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 't~',
             charge = 2/3,
             LeptonNumber = 0,
             GhostNumber = 0)

t__tilde__ = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'd~',
             charge = -1/3,
             LeptonNumber = 0,
             GhostNumber = 0)

d__tilde__ = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 's',
             antitexname = 's~',
             charge = -1/3,
             LeptonNumber = 0,
             GhostNumber = 0)

s__tilde__ = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'b~',
             charge = -1/3,
             LeptonNumber = 0,
             GhostNumber = 0)

b__tilde__ = b.anti()

a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             LeptonNumber = 0,
             GhostNumber = 0)

z = Particle(pdg_code = 23,
             name = 'z',
             antiname = 'z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'z',
             antitexname = 'z',
             charge = 0,
             LeptonNumber = 0,
             GhostNumber = 0)

w__plus__ = Particle(pdg_code = 24,
                     name = 'w+',
                     antiname = 'w-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'w+',
                     antitexname = 'w-',
                     charge = 1,
                     LeptonNumber = 0,
                     GhostNumber = 0)

w__minus__ = w__plus__.anti()

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0,
             LeptonNumber = 0,
             GhostNumber = 0)

h = Particle(pdg_code = 25,
             name = 'h',
             antiname = 'h',
             spin = 1,
             color = 1,
             mass = Param.MH,
             width = Param.WH,
             texname = 'H',
             antitexname = 'H',
             charge = 0,
             LeptonNumber = 0,
             GhostNumber = 0)

n1 = Particle(pdg_code = 3000001,
              name = 'n1',
              antiname = 'n1',
              spin = 2,
              color = 1,
              mass = Param.MN1,
              width = Param.WN1,
              texname = 'n1',
              antitexname = 'n1',
              charge = 0)

n2 = Particle(pdg_code = 3000002,
              name = 'n2',
              antiname = 'n2',
              spin = 2,
              color = 1,
              mass = Param.MN2,
              width = Param.WN2,
              texname = 'n2',
              antitexname = 'n2',
              charge = 0)

zd = Particle(pdg_code = 3000022,
              name = 'zd',
              antiname = 'zd',
              spin = 3,
              color = 1,
              mass = Param.MZD,
              width = Param.WZD,
              texname = 'zd',
              antitexname = 'zd',
              charge = 0)

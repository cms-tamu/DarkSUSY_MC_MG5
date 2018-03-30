# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 10.4.1 for Mac OS X x86 (64-bit) (April 11, 2016)
# Date: Fri 30 Mar 2018 06:48:55


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

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
             GhostNumber = 0,
             X = X[A],
             Y = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             GhostNumber = 0,
             X = X[Z],
             Y = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.ZERO,
                     width = Param.ZERO,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1,
                     GhostNumber = 0,
                     X = X[W],
                     Y = 0)

W__minus__ = W__plus__.anti()

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
             GhostNumber = 0,
             X = X[G],
             Y = 0)

ad = Particle(pdg_code = 3000022,
              name = 'ad',
              antiname = 'ad',
              spin = 3,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'ad',
              antitexname = 'ad',
              charge = 0,
              GhostNumber = 0,
              X = X[AD],
              Y = 0)

n1 = Particle(pdg_code = 1000022,
              name = 'n1',
              antiname = 'n1',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'n1',
              antitexname = 'n1',
              charge = 0,
              GhostNumber = 0,
              X = X[neu1bar],
              Y = 0)

n2 = Particle(pdg_code = 1000023,
              name = 'n2',
              antiname = 'n2',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'n2',
              antitexname = 'n2',
              charge = 0,
              GhostNumber = 0,
              X = X[neu2bar],
              Y = 0)

n3 = Particle(pdg_code = 1000025,
              name = 'n3',
              antiname = 'n3',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'n3',
              antitexname = 'n3',
              charge = 0,
              GhostNumber = 0,
              X = X[neu3bar],
              Y = 0)

n4 = Particle(pdg_code = 1000035,
              name = 'n4',
              antiname = 'n4',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'n4',
              antitexname = 'n4',
              charge = 0,
              GhostNumber = 0,
              X = X[neu4bar],
              Y = 0)

x1__plus__ = Particle(pdg_code = 1000024,
                      name = 'x1+',
                      antiname = 'x1-',
                      spin = 2,
                      color = 1,
                      mass = Param.ZERO,
                      width = Param.ZERO,
                      texname = 'x1+',
                      antitexname = 'x1-',
                      charge = 1,
                      GhostNumber = 0,
                      X = X[ch1],
                      Y = 0)

x1__minus__ = x1__plus__.anti()

x2__plus__ = Particle(pdg_code = 1000037,
                      name = 'x2+',
                      antiname = 'x2-',
                      spin = 2,
                      color = 1,
                      mass = Param.ZERO,
                      width = Param.ZERO,
                      texname = 'x2+',
                      antitexname = 'x2-',
                      charge = 1,
                      GhostNumber = 0,
                      X = X[ch2],
                      Y = 0)

x2__minus__ = x2__plus__.anti()

go = Particle(pdg_code = 1000021,
              name = 'go',
              antiname = 'go',
              spin = 2,
              color = 8,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'go',
              antitexname = 'go',
              charge = 0,
              GhostNumber = 0,
              X = X[gobar],
              Y = 0)

nD = Particle(pdg_code = 3000001,
              name = 'nD',
              antiname = 'nD',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'nD',
              antitexname = 'nD',
              charge = 0,
              GhostNumber = 0,
              X = X[neuDbar],
              Y = 0)

h01 = Particle(pdg_code = 25,
               name = 'h01',
               antiname = 'h01',
               spin = 1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'h01',
               antitexname = 'h01',
               charge = 0,
               GhostNumber = 0,
               X = X[h0],
               Y = 0)

h02 = Particle(pdg_code = 35,
               name = 'h02',
               antiname = 'h02',
               spin = 1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'h02',
               antitexname = 'h02',
               charge = 0,
               GhostNumber = 0,
               X = X[H0],
               Y = 0)

A0 = Particle(pdg_code = 36,
              name = 'A0',
              antiname = 'A0',
              spin = 1,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'A0',
              antitexname = 'A0',
              charge = 0,
              GhostNumber = 0,
              X = X[A0],
              Y = 0)

H__plus__ = Particle(pdg_code = 37,
                     name = 'H+',
                     antiname = 'H-',
                     spin = 1,
                     color = 1,
                     mass = Param.ZERO,
                     width = Param.ZERO,
                     texname = 'H+',
                     antitexname = 'H-',
                     charge = 1,
                     GhostNumber = 0,
                     X = X[H],
                     Y = 0)

H__minus__ = H__plus__.anti()

G0 = Particle(pdg_code = 250,
              name = 'G0',
              antiname = 'G0',
              spin = 1,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'G0',
              antitexname = 'G0',
              goldstone = True,
              charge = 0,
              GhostNumber = 0,
              X = X[G0],
              Y = 0)

G__plus__ = Particle(pdg_code = 251,
                     name = 'G+',
                     antiname = 'G-',
                     spin = 1,
                     color = 1,
                     mass = Param.ZERO,
                     width = Param.ZERO,
                     texname = 'G+',
                     antitexname = 'G-',
                     goldstone = True,
                     charge = 1,
                     GhostNumber = 0,
                     X = X[GP],
                     Y = 0)

G__minus__ = G__plus__.anti()

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
              GhostNumber = 0,
              X = X[ve],
              Y = 0)

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
              GhostNumber = 0,
              X = X[vm],
              Y = 0)

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
              GhostNumber = 0,
              X = X[vt],
              Y = 0)

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
                      GhostNumber = 0,
                      X = X[e],
                      Y = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.ZERO,
                       width = Param.ZERO,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       charge = -1,
                       GhostNumber = 0,
                       X = X[m],
                       Y = 0)

mu__plus__ = mu__minus__.anti()

tau__minus__ = Particle(pdg_code = 15,
                        name = 'tau-',
                        antiname = 'tau+',
                        spin = 2,
                        color = 1,
                        mass = Param.ZERO,
                        width = Param.ZERO,
                        texname = 'tau-',
                        antitexname = 'tau+',
                        charge = -1,
                        GhostNumber = 0,
                        X = X[ta],
                        Y = 0)

tau__plus__ = tau__minus__.anti()

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
             GhostNumber = 0,
             X = X[u],
             Y = 0)

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
             GhostNumber = 0,
             X = X[c],
             Y = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 't',
             antitexname = 't~',
             charge = 2/3,
             GhostNumber = 0,
             X = X[t],
             Y = 0)

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
             GhostNumber = 0,
             X = X[d],
             Y = 0)

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
             GhostNumber = 0,
             X = X[s],
             Y = 0)

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
             GhostNumber = 0,
             X = X[b],
             Y = 0)

b__tilde__ = b.anti()

sv1 = Particle(pdg_code = 1000012,
               name = 'sv1',
               antiname = 'sv1~',
               spin = 1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'sv1',
               antitexname = 'sv1~',
               charge = 0,
               GhostNumber = 0,
               X = X[sn1],
               Y = 0)

sv1__tilde__ = sv1.anti()

sv2 = Particle(pdg_code = 1000014,
               name = 'sv2',
               antiname = 'sv2~',
               spin = 1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'sv2',
               antitexname = 'sv2~',
               charge = 0,
               GhostNumber = 0,
               X = X[sn2],
               Y = 0)

sv2__tilde__ = sv2.anti()

sv3 = Particle(pdg_code = 1000016,
               name = 'sv3',
               antiname = 'sv3~',
               spin = 1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'sv3',
               antitexname = 'sv3~',
               charge = 0,
               GhostNumber = 0,
               X = X[sn3],
               Y = 0)

sv3__tilde__ = sv3.anti()

sl1__minus__ = Particle(pdg_code = 1000011,
                        name = 'sl1-',
                        antiname = 'sl1+',
                        spin = 1,
                        color = 1,
                        mass = Param.ZERO,
                        width = Param.ZERO,
                        texname = 'sl1-',
                        antitexname = 'sl1+',
                        charge = -1,
                        GhostNumber = 0,
                        X = X[sl1],
                        Y = 0)

sl1__plus__ = sl1__minus__.anti()

sl2__minus__ = Particle(pdg_code = 1000013,
                        name = 'sl2-',
                        antiname = 'sl2+',
                        spin = 1,
                        color = 1,
                        mass = Param.ZERO,
                        width = Param.ZERO,
                        texname = 'sl2-',
                        antitexname = 'sl2+',
                        charge = -1,
                        GhostNumber = 0,
                        X = X[sl2],
                        Y = 0)

sl2__plus__ = sl2__minus__.anti()

sl3__minus__ = Particle(pdg_code = 1000015,
                        name = 'sl3-',
                        antiname = 'sl3+',
                        spin = 1,
                        color = 1,
                        mass = Param.ZERO,
                        width = Param.ZERO,
                        texname = 'sl3-',
                        antitexname = 'sl3+',
                        charge = -1,
                        GhostNumber = 0,
                        X = X[sl3],
                        Y = 0)

sl3__plus__ = sl3__minus__.anti()

sl4__minus__ = Particle(pdg_code = 2000011,
                        name = 'sl4-',
                        antiname = 'sl4+',
                        spin = 1,
                        color = 1,
                        mass = Param.ZERO,
                        width = Param.ZERO,
                        texname = 'sl4-',
                        antitexname = 'sl4+',
                        charge = -1,
                        GhostNumber = 0,
                        X = X[sl4],
                        Y = 0)

sl4__plus__ = sl4__minus__.anti()

sl5__minus__ = Particle(pdg_code = 2000013,
                        name = 'sl5-',
                        antiname = 'sl5+',
                        spin = 1,
                        color = 1,
                        mass = Param.ZERO,
                        width = Param.ZERO,
                        texname = 'sl5-',
                        antitexname = 'sl5+',
                        charge = -1,
                        GhostNumber = 0,
                        X = X[sl5],
                        Y = 0)

sl5__plus__ = sl5__minus__.anti()

sl6__minus__ = Particle(pdg_code = 2000015,
                        name = 'sl6-',
                        antiname = 'sl6+',
                        spin = 1,
                        color = 1,
                        mass = Param.ZERO,
                        width = Param.ZERO,
                        texname = 'sl6-',
                        antitexname = 'sl6+',
                        charge = -1,
                        GhostNumber = 0,
                        X = X[sl6],
                        Y = 0)

sl6__plus__ = sl6__minus__.anti()

su1 = Particle(pdg_code = 1000002,
               name = 'su1',
               antiname = 'su1~',
               spin = 1,
               color = 3,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'su1',
               antitexname = 'su1~',
               charge = 2/3,
               GhostNumber = 0,
               X = X[su1],
               Y = 0)

su1__tilde__ = su1.anti()

su2 = Particle(pdg_code = 1000004,
               name = 'su2',
               antiname = 'su2~',
               spin = 1,
               color = 3,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'su2',
               antitexname = 'su2~',
               charge = 2/3,
               GhostNumber = 0,
               X = X[su2],
               Y = 0)

su2__tilde__ = su2.anti()

su3 = Particle(pdg_code = 1000006,
               name = 'su3',
               antiname = 'su3~',
               spin = 1,
               color = 3,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'su3',
               antitexname = 'su3~',
               charge = 2/3,
               GhostNumber = 0,
               X = X[su3],
               Y = 0)

su3__tilde__ = su3.anti()

su4 = Particle(pdg_code = 2000002,
               name = 'su4',
               antiname = 'su4~',
               spin = 1,
               color = 3,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'su4',
               antitexname = 'su4~',
               charge = 2/3,
               GhostNumber = 0,
               X = X[su4],
               Y = 0)

su4__tilde__ = su4.anti()

su5 = Particle(pdg_code = 2000004,
               name = 'su5',
               antiname = 'su5~',
               spin = 1,
               color = 3,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'su5',
               antitexname = 'su5~',
               charge = 2/3,
               GhostNumber = 0,
               X = X[su5],
               Y = 0)

su5__tilde__ = su5.anti()

su6 = Particle(pdg_code = 2000006,
               name = 'su6',
               antiname = 'su6~',
               spin = 1,
               color = 3,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'su6',
               antitexname = 'su6~',
               charge = 2/3,
               GhostNumber = 0,
               X = X[su6],
               Y = 0)

su6__tilde__ = su6.anti()

sd1 = Particle(pdg_code = 1000001,
               name = 'sd1',
               antiname = 'sd1~',
               spin = 1,
               color = 3,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'sd1',
               antitexname = 'sd1~',
               charge = -1/3,
               GhostNumber = 0,
               X = X[sd1],
               Y = 0)

sd1__tilde__ = sd1.anti()

sd2 = Particle(pdg_code = 1000003,
               name = 'sd2',
               antiname = 'sd2~',
               spin = 1,
               color = 3,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'sd2',
               antitexname = 'sd2~',
               charge = -1/3,
               GhostNumber = 0,
               X = X[sd2],
               Y = 0)

sd2__tilde__ = sd2.anti()

sd3 = Particle(pdg_code = 1000005,
               name = 'sd3',
               antiname = 'sd3~',
               spin = 1,
               color = 3,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'sd3',
               antitexname = 'sd3~',
               charge = -1/3,
               GhostNumber = 0,
               X = X[sd3],
               Y = 0)

sd3__tilde__ = sd3.anti()

sd4 = Particle(pdg_code = 2000001,
               name = 'sd4',
               antiname = 'sd4~',
               spin = 1,
               color = 3,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'sd4',
               antitexname = 'sd4~',
               charge = -1/3,
               GhostNumber = 0,
               X = X[sd4],
               Y = 0)

sd4__tilde__ = sd4.anti()

sd5 = Particle(pdg_code = 2000003,
               name = 'sd5',
               antiname = 'sd5~',
               spin = 1,
               color = 3,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'sd5',
               antitexname = 'sd5~',
               charge = -1/3,
               GhostNumber = 0,
               X = X[sd5],
               Y = 0)

sd5__tilde__ = sd5.anti()

sd6 = Particle(pdg_code = 2000005,
               name = 'sd6',
               antiname = 'sd6~',
               spin = 1,
               color = 3,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'sd6',
               antitexname = 'sd6~',
               charge = -1/3,
               GhostNumber = 0,
               X = X[sd6],
               Y = 0)

sd6__tilde__ = sd6.anti()

ghG = Particle(pdg_code = 9000001,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG~',
               charge = 0,
               GhostNumber = 1,
               X = X[ghG],
               Y = 0)

ghG__tilde__ = ghG.anti()

ghA = Particle(pdg_code = 9000002,
               name = 'ghA',
               antiname = 'ghA~',
               spin = -1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghA',
               antitexname = 'ghA~',
               charge = 0,
               GhostNumber = 1,
               X = X[ghA],
               Y = 0)

ghA__tilde__ = ghA.anti()

ghZ = Particle(pdg_code = 9000003,
               name = 'ghZ',
               antiname = 'ghZ~',
               spin = -1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghZ',
               antitexname = 'ghZ~',
               charge = 0,
               GhostNumber = 1,
               X = X[ghZ],
               Y = 0)

ghZ__tilde__ = ghZ.anti()

ghWp = Particle(pdg_code = 9000004,
                name = 'ghWp',
                antiname = 'ghWp~',
                spin = -1,
                color = 1,
                mass = Param.ZERO,
                width = Param.ZERO,
                texname = 'ghWp',
                antitexname = 'ghWp~',
                charge = 1,
                GhostNumber = 1,
                X = X[ghWp],
                Y = 0)

ghWp__tilde__ = ghWp.anti()

ghWm = Particle(pdg_code = 9000005,
                name = 'ghWm',
                antiname = 'ghWm~',
                spin = -1,
                color = 1,
                mass = Param.ZERO,
                width = Param.ZERO,
                texname = 'ghWm',
                antitexname = 'ghWm~',
                charge = -1,
                GhostNumber = 1,
                X = X[ghWm],
                Y = 0)

ghWm__tilde__ = ghWm.anti()


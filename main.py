#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import numpy as np  
import matplotlib.pyplot as plt

def visu_point(matPoint,style):
    # matPoint contient les coordonnées des points 
    x = matPoint[0, :]
    y = matPoint[1, :]
    plt.plot(x, y, style)
    
def mat_Translation_h(tx,ty):
    mat = np.array([[1, 0, tx],
                    [0, 1, ty],
                    [0, 0, 1]])
    return mat

def mat_Rotation_h(theta):
    mat = np.array([[np.cos(theta), np.sin(theta), 0],
                    [-np.sin(theta), np.cos(theta), 0],
                    [0, 0, 1]])
    return mat

def mat_Scale_h(sx,sy):
    mat = np.array([[sx, 0, 0],
                    [0, sy, 0],
                    [0, 0, 1]])
    return mat

#première partie : afficher la pente
def visu_BezierCubic(matPointControl,str):
    
    n=50
    
    mt = np.linspace(0,1.,n)  
    matt = np.ones((4,n))
    matt[1,:] = mt  # ligne avec les t
    matt[2,:] = mt*mt  # ligne avec les t*t
    matt[3,:] = mt*mt*mt
    
    matBezier4 = np.array([[1, 0, 0, 0], 
                           [-3, 3, 0, 0], 
                           [3, -6, 3, 0],
                           [-1, 3, -3, 1]])    
    
    matPointligne = np.dot(np.dot(matt.T,matBezier4),matPointControl.T)
    matPoint=matPointligne.T  # on transpose

    visu_point(matPointControl,'k.')
    visu_point(matPointControl,'g:')
    visu_point(matPoint,str)

matPointControl2 = np.array([[15,55,25, 60],
                            [60,45,20, 15]
                            ])
visu_BezierCubic(matPointControl2, 'k-')

#deuxième partie : afficher le triangle

def matP_homogene(matP):  
    # la matrice des points écrits en coordonnées homogènes
    nP=matP.shape[1] 
    matP_h = np.concatenate((matP,np.ones((1,nP))),0)
    return matP_h

xmin, xmax = plt.xlim(-5, 70)
ymin, ymax = plt.ylim(-5, 70)

matP=np.array([[0, 2, 0, 0],
                [0, 2, 4, 0],
                [1, 1, 1, 1]])
    
matP = np.dot(mat_Translation_h(15, 60), matP)
    
def affiche_polygone(matP, string):
    x = matP[0, :]
    y = matP[1, :]
    plt.plot(x, y, string)

affiche_polygone(matP, 'b-')
var1 = -matP[0][0]
var2 = -matP[1][0]
    
def parcoursBezier(matPtControle, t, var):
    matPoint = np.array([[1, var, var * var]])
    derive = np.array([[-3, -3, 0, 0],
                        [6, -12, 6, 0],
                        [-3, 9, -9, 3],
                        [1, 1, 1, 1]])
    x = np.dot(matPtControle, derive)
    x = np.dot(matPoint, x)
    t1 = np.tan(x[0][0])
    
    var1 = matP[0][0]
    var2 = matP[1][0]
    ligneX = (1 - t)*(1 - t)*(1 - t) * matPointControl[0][0] + 3*t*(1 - t)*(1 - t) * matPointControl[0][1] + 3*t*t * (1-t) * matPointControl[0][2] + t*t*t * matPointControl[0][3] 
    ligneY = (1 - t)*(1 - t)*(1 - t) * matPointControl[1][0] + 3*t*(1 - t)*(1 - t) * matPointControl[1][1] + 3*t*t * (1-t) * matPointControl[1][2] + t*t*t * matPointControl[1][3] 

    matrice = np.dot(mat_Translation_h(-var1, -var2), matP)
    matrice = np.dot(mat_Rotation_h(t1), matrice)
    matrice = np.dot(mat_Scale_h(t+1, t+1), matrice)
    matrice = np.dot(mat_Translation_h(ligneX, ligneY), matrice)
    affiche_polygone(matrice, 'r-')
    
    
    
matPointControl = np.array([[15,55,25, 60],
                            [60,45,20, 15],
                            [1, 1, 1, 1]])

liste = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

for i in liste:
    parcoursBezier(matPointControl, i, 0.3)
    

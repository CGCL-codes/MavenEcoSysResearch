# Analysejar description

Usage pattern:
```
Java -jar analyseJar.jar -c callstack -j jar_to_analyse -option
```

Option usage:
```
 -bd,--CVEBlockDepth                  get block depth of target CVE
 -c,--callStackFile <arg>             File thatcontains call stack
 -cl,--ConstraintLength               get the number of constraint along
                                      the path
 -co,--ConstraintOperand              get the operand of constraint along
                                      the path
 -cr,--ConstraintVariableReturnType   get information about return type of
                                      the constraint variable
 -cs,--CallSiteInfo                   get information about the call
                                      site:Guarded@Returned@AsPara
 -cv,--ConstraintVariable             get the type of variable involved in
                                      the constraint along the path
 -h,--help                            Print usage
 -j,--jarName <arg>                   Jar file that to be analysed
 -md,--MethodBlockDepth               get block depth of method in target
                                      CVE
 -pc,--PathCoverage                   get path coverage of the path
```

Example:
```
Java -jar analyseJar.jar -c ./example/callstack/CVE-2016-9487@org.idpf:epubcheck:4.0.1 -j ./example/jar_to_analyse/epubcheck-4.0.1.jar -co
````````````
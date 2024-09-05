options dlcreatedir;
libname outputs "/workflow/outputs"; /* All outputs must go to this directory at workflow/inputs/<NAME OF OUTPUT>y */ 

/* Load in datasetA */
data _null__;
    infile '/workflow/inputs/data_path_a' truncover;
    input data_path $CHAR100.;
    call symputx('data_path_a', data_path, 'G');
run;
libname datasetA "&data_path_a.";

/* Load in datasetB */
data _null__;
    infile '/workflow/inputs/data_path_b' truncover;
    input data_path $CHAR100.;
    call symputx('data_path_b', data_path, 'G');
run;
libname datasetB "&data_path_b.";

/* Load in datasetC */
data _null__;
    infile '/workflow/inputs/data_path_c' truncover;
    input data_path $CHAR100.;
    call symputx('data_path_c', data_path, 'G');
run;
libname datasetC "&data_path_c.";

/* Write the final ADAM output */
data outputs.adam;
    merge datasetA.sv datasetB.ts datasetC.ta;
run;



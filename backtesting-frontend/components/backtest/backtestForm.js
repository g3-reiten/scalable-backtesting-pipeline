import { useRouter } from 'next/router';
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as Yup from 'yup';
import { Layout } from '../account/Layout';
import { BacktestService } from '../../services';

export function BacktestForm() { 
    const router = useRouter();
    const validationSchema = Yup.object().shape({
        name: Yup.string()
        .required('Name is required'),
        stratagy: Yup.string()
            .required('Stratagy Name is required'),
        cash: Yup.string()
            .required('Cash is required'),
        commision: Yup.string()
            .required('Commision is required'),
    });
    const formOptions = { resolver: yupResolver(validationSchema) };

    // get functions to build form with useForm() hook
    const { register, handleSubmit, formState } = useForm(formOptions);
    const { errors } = formState;

    function onSubmit(data) {
        BacktestService.getBacktestOutput(data)
    }

    return (
       <Layout>
            <div className="card">
                <h4 className="card-header">BackTest</h4>
                <div className="card-body">
                    <form onSubmit={handleSubmit(onSubmit)}>
                        <div className="form-group">
                            <label>Name</label>
                            <input name="name" type="text" {...register('name')} className={`form-control ${errors.name ? 'is-invalid' : ''}`} />
                            <div className="invalid-feedback">{errors.name?.message}</div>
                        </div>
                        <div className="form-group">
                            <label>Stratagy</label>
                            <select id ="stratagy" name="stratagy" {...register('stratagy')} className={`form-control ${errors.stratagy ? 'is-invalid' : ''}`}>
                                <option>SmaCross</option>
                            </select>
                            <div className="invalid-feedback">{errors.stratagy?.message}</div>
                        </div>
                        <div className="form-group">
                            <label>Cash</label>
                            <input name="cash" type="test" {...register('cash')} className={`form-control ${errors.cash ? 'is-invalid' : ''}`} />
                            <div className="invalid-feedback">{errors.cash?.message}</div>
                        </div>
                        <div className="form-group">
                            <label>Commission</label>
                            <input name="commission" type="number" {...register('commision')} className={`form-control ${errors.commision ? 'is-invalid' : ''}`} />
                            <div className="invalid-feedback">{errors.commision?.message}</div>
                        </div>
                        <button disabled={formState.isSubmitting} className="btn btn-primary">
                            {formState.isSubmitting && <span className="spinner-border spinner-border-sm mr-1"></span>}
                            Submit
                        </button>
                    </form>
                </div>
            </div>
            </Layout>
    );
}

import { useRouter } from 'next/router';
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as Yup from 'yup';
import axios from "axios";
import { Layout } from './account/Layout';


export default Login;

function Login() {
    const router = useRouter();

    const validationSchema = Yup.object().shape({
        username: Yup.string().required('Username is required'),
        password: Yup.string().required('Password is required')
    });
    const formOptions = { resolver: yupResolver(validationSchema) };

    const { register, handleSubmit, formState } = useForm(formOptions);
    const { errors } = formState;

    function onSubmit({ username, password }) {
        axios({
            method: "POST",
            url:"http://127.0.0.1:5000/login",
            data:{
              email: username,
              password: password
             }
          })
          .then((response) => {
            sessionStorage.setItem('token', response.data.token)
          }).catch((error) => {
            if (error.response) {
              console.log(error.response)
              console.log(error.response.status)
              console.log(error.response.headers)
              }
          })  
    }
    
    return (
        <Layout>
            <div className="card">
                <h4 className="card-header">Login</h4>
                <div className="card-body">
                    <form onSubmit={handleSubmit(onSubmit)}>
                        <div className="form-group">
                            <label>Username</label>
                            <input name="username" type="text" {...register('username')} className={`form-control ${errors.username ? 'is-invalid' : ''}`} />
                            <div className="invalid-feedback">{errors.username?.message}</div>
                        </div>
                        <div className="form-group">
                            <label>Password</label>
                            <input name="password" type="password" {...register('password')} className={`form-control ${errors.password ? 'is-invalid' : ''}`} />
                            <div className="invalid-feedback">{errors.password?.message}</div>
                        </div>
                        <button disabled={formState.isSubmitting} className="btn btn-primary">
                            {formState.isSubmitting && <span className="spinner-border spinner-border-sm mr-1"></span>}
                            Login
                        </button>
                        {/* <Link href="/account/register" className="btn btn-link">Register</Link> */}
                    </form>
                </div>
            </div>
        </Layout>
    );
}
// axios.get('http://127.0.0.1:5000/user', {
//         headers: {
//             'x-access-token': sessionStorage.getItem('token')
//         }
//         }).then((response) => {
//             console.log(response)
//         }).catch((error) => {
//         if (error.response) {
//           console.log(error.response)
//           console.log(error.response.status)
//           console.log(error.response.headers)
//           }
//         })